from ast import parse
from fileinput import filename

from bs4 import BeautifulSoup

from Spider_base.base_spider import BaseSpider
import os
import queue
import threading
import time


class IssueSpider(BaseSpider):

    def __init__(self):
        super().__init__()
        self.setup()
        self.issue_solution_list = []
        self.log_filename = 'ECS_Spider.log'
        self.url = "https://developer.aliyun.com/ask/product/all-3?pageNum="
        self.queue = queue.Queue()

        if os.path.exists(self.log_filename):
            os.remove(self.log_filename)

    def start_requests(self):
        start_time = time.time()
        num_pages = 50
        for current_page in range(1, num_pages + 1):
            url = self.url + str(current_page)
            self.queue.put(url)

        for _ in range(5):  # 启动 5 个线程
            t = threading.Thread(target=self.worker)
            t.start()

        self.queue.join()
        end_time = time.time()
        print(f"程序运行总时间：{end_time - start_time}秒")
        self.logger.info(f"程序运行总时间：{end_time - start_time}秒")


    def worker(self):
        while True:
            url = self.queue.get()
            response = self.request_handler(url, headers=self.config['request_headers'])
            if response.status_code == 200:
                self.parse(response.text)
            else:
                self.logger.error(f"Error:{response.status_code}[page={url.split('=')[-1]}请求失败]")
            self.queue.task_done()



    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        solved_questions = soup.find_all('div', class_='askProduct-list')
        for solved_question in solved_questions:
            status_div = solved_question.find('div', class_='askProduct-item-status')
            if status_div:
                status = status_div.text.strip()
                if status == '已解决':
                    question_title = solved_question.find('h3').text.strip()
                    base_url = "https://developer.aliyun.com"
                    answer_link = solved_question.find('a', class_='askProduct-item-title-text')['href']
                    answer_link = base_url + answer_link
                    answer_response = self.request_handler(answer_link, headers=self.config['request_headers'])
                    if answer_response.status_code == 200:
                        answer_soup = BeautifulSoup(answer_response.text, 'html.parser')
                        solution_div = answer_soup.find('div', class_='answer-right')
                        if solution_div:
                            solution = solution_div.find('div', class_='respond-content').text.strip()

                    self.issue_solution_list.append({'question_title': question_title, 'answer_link': answer_link, 'official_solution': solution })



    def save_data(self):
        self.storage.save_data(self.issue_solution_list,filename="spider_data.json")
        self.logger.info(f"成功保存{len(self.issue_solution_list)}条数据")



if __name__ == '__main__':
    IssueSpider = IssueSpider()
    IssueSpider.start_requests()
    IssueSpider.save_data()


