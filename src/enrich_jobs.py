# %%
import json
import requests

with open("data/data.json", "r") as f:
    data = json.load(f)
    
base_url = "http://yoda.bds.lab:8008"

chat_id = "15dd4f14-0c0a-4cde-98b0-0f3a358e89bb"
i = 0
for key, val in data.items():
    i+=1
    print(i)
    #id = "5845062"   
    #val = data[id]
    prompt = val["text"]
    req = f"http://yoda.bds.lab:8008/api/chat/{chat_id}/question?prompt={prompt}"
    result = requests.post(req)
    
    d = eval(result.json())
    data[key]["features"] = d["choices"][0]["text"]
    if i > 10:
        break

with open("data/data_enrichted.json", "w") as f:
    json.dump(data, f, indent=4)
    
print("done")