import json
import xlrd
from collections import defaultdict

def defaultAnswer():
    return "Please select one of the topics below or ask directly your question:"

def getNameAnswer(string):
    return string.split("\n")

def unmergedValue(thesheet, rowx, colx):
    for crange in thesheet.merged_cells:
        rlo, rhi, clo, chi = crange
        if rowx in range(rlo, rhi):
            if colx in range(clo, chi):
                return thesheet.cell_value(rlo, clo)
    # if you reached this point, it's not in any merged cells
    return thesheet.cell_value(rowx, colx)


def ctree():
    """ One of the python gems. Making possible to have dynamic tree structure.

    """
    return defaultdict(ctree)


def build_leaf(name, leaf):
    """ Recursive function to build desired custom tree structure

    """
    res = {name:"last"}
    #print(leaf.items())
    # add children node if the leaf actually has any children
    if len(leaf.keys()) == 1:
        res[name] = [build_leaf(k, v) for k, v in leaf.items()]
    elif len(leaf.keys()) > 0:
        res[name] = [build_leaf(k, v) for k, v in leaf.items()]

    return res


book = xlrd.open_workbook("FAQ-example.xlsx")
base_sheet = book.sheet_by_index(0)

#Number of columns on the left that are not used for the decision tree 
left_colums=3

tree = ctree()
for i in range(1, base_sheet.nrows):
    row = base_sheet.row(i)
    row_0 = unmergedValue(base_sheet, i, 0)
    # usage of python magic to construct dynamic tree structure and
    # basically grouping exel values under their parents
    leaf = tree[row_0]
    for cid in range(1, len(row)-left_colums):
        if unmergedValue(base_sheet, i, cid) == '':
            continue
        else:
            leaf = leaf[unmergedValue(base_sheet, i, cid)]

# building a custom tree structure
res = []
for name, leaf in tree.items():
    res.append(build_leaf(name, leaf))

"""
JUST FOR TESTING POURPOSES

# printing results into the terminal
print(json.dumps(res[0]))
test = {"CCoE MEMBER\nTipical Questions for CCoE are": 
    [
    {"Accounts": 
        [
            {"Account Vend Sandbox": "last"}, 
            {"Account Vend Application": "last"}
        ]
    }, 
    {"Federation roles and access": "last"}
    ]
}
"""

qna = {"qna": []}

def fillQnA(d):
    for text, list_buttons in d.items():
        text_list = getNameAnswer(text)
        name_value = text_list[0]
        if len(text_list) <= 1:
            answer_value = defaultAnswer()
        else:
            answer_value = text_list[1]
        #get the buttons
        buttons=[]
        for i in list_buttons:
            key_value=list(i.keys())[0]
            key_value_name=getNameAnswer(key_value)[0]
            buttons.append({"text":key_value_name,"value":key_value_name})
        temp_dict = {
            "qid":name_value.replace(" ",""),
            "type": "qna",
            "q":name_value.split("/"),
            "a":answer_value,
            "r":{
                    "buttons": buttons,
                    "subTitle": "",
                    "imageUrl": "",
                    "title": "button"
                }
            }
        qna["qna"].append(temp_dict)    
        for j in list_buttons: 
            key_value=list(j.keys())[0]
            if isinstance(j[key_value], list):
                fillQnA(j)
            else:
                continue
            
fillQnA(res[0])
#print(qna)




def metodo_split_preguntas_en_lista(preguntas_string):
    lista_con_preguntas=preguntas_string.split("\n")
    return lista_con_preguntas


for r in range(1, base_sheet.nrows):
    id1=base_sheet.cell(r,-4).value 
    questions=base_sheet.cell(r,-3).value
    answer=base_sheet.cell(r,-2).value
    link=base_sheet.cell(r,-1).value
    temp_dict={"qid":id1,
                "q":metodo_split_preguntas_en_lista(questions)+[id1],
                "a":answer+''+link,
                "r": {
                    "title": "",
                     "imageUrl": ""
                    }
                }
    qna["qna"].append(temp_dict)



with open('qna.json', 'w') as fp:
    json.dump(qna, fp)