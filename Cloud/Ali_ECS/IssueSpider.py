from ast import parse
from fileinput import filename

from bs4 import BeautifulSoup

from Spider_base.base_spider import BaseSpider
import json
import os


class IssueSpider(BaseSpider):

    def __init__(self):
        super().__init__()
        self.setup()
        self.issue_solution_list = []
        self.log_filename = 'ECS_Spider.log'
        self.url = f"https://developer.aliyun.com/ask/product/all-3?pageNum="

        if os.path.exists(self.log_filename):
            os.remove(self.log_filename)

    def start_requests(self):
        url = self.url
        num_pages = 2
        for current_page in range(1, num_pages + 1):
            url = url + str(current_page)
            response = self.request_handler(url, headers=self.config['request_headers'])
            if response.status_code == 200:
                self.parse(response.text)
            else:
                self.logger.error(f"Error:{response.status_code}[page={current_page}请求失败]")

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        solved_questions = soup.find_all('div', class_='askProduct-list')
        for solved_question in solved_questions:
            status_div = solved_question.find('div', class_='askProduct-item-status')
            if status_div:
                status = status_div.text.strip()
                if status == '已解决':
                    question_title = solved_question.find('h3').text.strip()
                    # solution = solved_question.find('span', class_='askProduct-item-desc-content').text.strip()
                    question_link = solved_question.find('a', class_='askProduct-item-title-text')['href']
                    self.issue_solution_list.append({'question_title': question_title, 'question_link': question_link})
                    print(self.issue_solution_list)



    def save_data(self):
        self.storage.save_data(self.issue_solution_list,filename="spider_data.json")
        self.logger.info(f"成功保存{len(self.issue_solution_list)}条数据")



if __name__ == '__main__':
    IssueSpider = IssueSpider()
    IssueSpider.start_requests()
    IssueSpider.save_data()


