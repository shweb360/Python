class AnonymousSurvey():
    # 收集匿名调查问卷的答案
    def __init__(self,question):
        self.question=question
        self.responses=[]
    # 显示调查问卷
    def show_question(self):
        print(self.question)
    
    # 存储单份调查答卷
    def store_question(self,new_question):
        self.responses.append(new_question)

    def show_result(self):
        print("调查结果：")
        for response in self.responses:
            print(' - ' + response)

