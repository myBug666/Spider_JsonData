import requests

class Read_Url():

    def find_read(self):
        file_name = 'url.txt'
        with open(file_name) as file_obj:
            import pandas as pd
            with pd.ExcelWriter(r"cishan.xlsx") as writer:
                for index,content in enumerate(file_obj):
                    content = content.strip('\n')
                    print(content)
                    json_data = requests.get(content)
                    data = json_data.json().get('cData').get('list')
                    # 循环遍历每一条内容
                    rows = [[row.get('detail_href'),row.get('mainTitle'),row.get('publishTime'),row.get('_orderId')] for row in data]
                    dataframe = pd.DataFrame(rows, columns=["链接", "标题", "日期", "工单"])
                    dataframe.to_excel(writer, sheet_name="sheet" + str(index), index=False,engine="openpyxl")

if __name__ == '__main__':
    el = Read_Url()
    el.find_read()