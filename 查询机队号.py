
aircraft=[{"msn":"B6022","fleet_num":"001"},{"msn":"B6023","fleet_num":"002"},{"msn":"B6024","fleet_num":"003"},{"msn":"B6031","fleet_num":"004"}]


fine_plane=str(input("请输入机号："))

# 用以下IF语句纠正输入的可能错误。

if "b" in fine_plane:
    # 或者选择这一句，转换小写的"b"成大写的"B"。
    # fine_plane=fine_plane.upper()
    fine_plane="B"+fine_plane[1:]
elif "B" not in fine_plane:
    fine_plane = "B" + fine_plane


for plane in aircraft:

    if plane["msn"] == fine_plane:
        print("%s飞机的机队号为%s" % (plane["msn"],plane["fleet_num"]))
        break
else:
    print("找不到你的飞机")
print("欢迎再来！")

