

import os,json,time


"""
    main.json[
        {"name":存档名称,
        "file":存档文件名(时间格式),},
        ...
        ]

    save_json{
        自行设定
    }
"""


class Saves():
    #初始化存档集对象
    def __init__(self,folder_path,json_suffix="json"):
        self.folder_path=folder_path
        self.suffix=json_suffix
        self.lists=None    #存档目录


        #检查目录并载入list文件
        os.makedirs(self.folder_path,exist_ok=True)
        #路径存在时尝试读取
        if os.path.exists(f"{self.folder_path}/list.{self.suffix}"):
            try:
                with open(f"{self.folder_path}/list.{self.suffix}","r",encoding="utf-8") as f:    self.lists=json.load(f)
            except json.JSONDecodeError:
                self.lists = []
                self.update_lists()
        else:
            with open(f"{self.folder_path}/list.{self.suffix}","w",encoding="utf-8") as f:    self.lists=[]



    """存档目录处理"""
    #获取单个存档文件名(遍历查找)
    def get_filename(self,save_name):
        for save in self.lists:
            if save["name"]==save_name:    return f"{save['filename']}"
        else:    raise FileNotFoundError(f'save "{save_name}" not found')

    #获取存档列表
    def get_lists(self):
        return [each["name"] for each in self.lists]

    #更新存档目录
    def update_lists(self):
        with open(f"{self.folder_path}/list.{self.suffix}","w",encoding="utf-8") as f:
            json.dump(self.lists,f,ensure_ascii=False,indent=4)



    """存档处理"""
    #创建存档,若存档名已存在报错,更新目录
    def sett(self,save_name,parameter):
        try:
            self.get_filename(save_name)
            raise FileExistsError(f'save "{save_name}" already exists')
        except FileNotFoundError: 
            load_time=str( time.strftime("%y%m%d_%H%M%S",time.localtime()) )
            Save(f"{self.folder_path}/{load_time}.{self.suffix}").sett(parameter)
            self.lists.append({"name":save_name,"filename":load_time})
            self.update_lists()
    #删除存档,更新目录
    def dele(self,save_name):
        filename=self.get_filename(save_name)
        Save(f"{self.folder_path}/{filename}.{self.suffix}").dele()
        self.lists=[save for save in self.lists if  save["name"]==save_name]
        self.update_lists()
        return None
    #获取存档
    def get(self,save_name):
        return Save(f"{self.folder_path}/{self.get_filename(save_name)}.{self.suffix}").get()
    #更新存档
    def update(self,save_name,parameter):
        self.get_filename(save_name)
        Save(f"{self.folder_path}/{self.get_filename(save_name)}.{self.suffix}").update(parameter)





class Save():
    #初始化存档对象
    def __init__(self,file_path):    self.path=file_path

    """存档对象处理"""
    #创建: 已存在存档时报错
    def sett(self,parameter):
        if os.path.exists(self.path):
            raise FileExistsError(f'path "{self.path}" already exists')
        else:
            with open(self.path,"w",encoding="utf-8") as f:
                json.dump(parameter,f,ensure_ascii=False,indent=4)
    #删除: 不存在存档时报错
    def dele(self):
        if os.path.exists(self.path):    os.remove(self.path)
        else:    raise FileNotFoundError(f'path "{self.path}" not found')
    #获取: 不存在存档时报错
    def get(self):
        if os.path.exists(self.path):
            with open(self.path,"r",encoding="utf-8") as f:    return json.load(f)
        else:    raise FileNotFoundError(f'path "{self.path}" not found')
    #更新: 不存在存档时报错
    def update(self,parameter):
        if os.path.exists(self.path):
            with open(self.path,"w",encoding="utf-8") as f:
                json.dump(parameter,f,ensure_ascii=False,indent=4)
        else:    raise FileNotFoundError(f'path "{self.path}" not found')





if __name__=="__main__":
    pass





