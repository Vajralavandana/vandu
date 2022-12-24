import pandas as pd
df = pd.read_csv("C://Users//Vandana//Downloads//username.csv")
# print(df.to_string())
print(df)

dataset = {"vehicle": ["verna", "himalaya"], "type": ["car", "bike"]}
data_frame = pd.DataFrame(dataset)
print(data_frame)
frame_ind = pd.DataFrame(dataset, index=["0", "1"])
print(frame_ind)
print(data_frame.loc[0])
print(data_frame.loc[[0], ["vehicle"]])
print(data_frame.loc[:, ["vehicle"]])
print(data_frame.loc[[0, 1], ["vehicle"]])
print(data_frame.loc[[0, 1]])
print(data_frame.loc[[]])


import pandas as pp
pa = pp.read_csv("C://Users//Vandana//Downloads//test_csv1.csv")
print(pa)
ds = {"name": ["smith", "mary"], "age": ["20", "22"]}
d_s = pp.DataFrame(ds)
print(d_s)

f_id = pp.DataFrame(ds, index=["i", "ii"])
print(f_id)

print(d_s.loc[0])
print(d_s.loc[[1], ["name"]])
print(d_s.loc[[0, 1], ["name"]])
print(d_s.loc[:, ["age"]])
print(d_s.loc[[0, 1]])
print(d_s.loc[[]])

# lst = [1, 4, 7]
# ser = pd.Series(lst)
# print(ser)
#
# data = {"day1": "sunday", "day2": "monday"}
# ser_data = pd.Series(data)
# print(ser_data)


