import json
firm_dict = {}
averang_profit = []
with open('7.txt') as f:
    lines = f.readlines()
    for line in lines:
        name, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firm_dict[name] = profit
        if profit > 0:
            averang_profit.append(profit)
averang_profit = sum(averang_profit) / len(averang_profit)
out_info = [firm_dict, {'averang_profit': averang_profit}]

with open('7.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('7.json') as f_json:
    print(json.load(f_json))