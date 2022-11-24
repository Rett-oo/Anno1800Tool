import json
import os


a = open("C:\\Users\\user\\Desktop\\filepathes.txt", "w", encoding="utf-8")

for adress, dirs, files in os.walk("E:\\Python\\Anno1800Tool\\resourсes\\images"):
    for file in files:
        file_path = os.path.join(adress, file)
        l = file_path.split('\\')[4:]
        def gen_json():
            json_dict = {}
            file_name = l.pop(-1)
            for i in l:
                try:
                    if i in list(json_dict.keys()):
                        print("uje est!")
                    json_dict.update({i: l[l.index(i)+1]})

                except IndexError:
                    pass

            print(json_dict)
            return json_dict



        gen_json()




        # a.write(str(gen_json()))
        # def gen_json(l,d=dict()):
        #     tmp = {}
        #     if not d:
        #         d["name"] = l.pop(-1)
        #     tmp["children"]=d
        #     tmp["name"]=l.pop(-1)
        #     return gen_json(l,tmp) if l else tmp

        # print(json.dumps(gen_json(l), ensure_ascii=False))


a.close()