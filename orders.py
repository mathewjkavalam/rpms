def order_guides_ascendingly_called_list(guidecalledcountdictionary=dict() ,guideteamremaining=dict(),priority=list(),classs=str()):
    from random import shuffle

    guideteam_in_class = guideteamremaining[classs]
    sorted_guideteam = list()
    for count in range(0, max( guidecalledcountdictionary.values())+1 ):
        for guideteam in guideteam_in_class:
            guide = guideteam[0]
            if  guidecalledcountdictionary[guide] == count:
                sorted_guideteam.append(guideteam)
    #overiding ; always giving deafult the priority

    shuffle(priority)
    defaults_team = list()
    for fac in priority:
        for guideteam in guideteam_in_class:
            guide = guideteam[0]
            if fac == guide:
                defaults_team.append(guideteam)
    for defaultgt in defaults_team:
        sorted_guideteam.insert(0,defaultgt)

    return sorted_guideteam

def order_faculty_areaofinterest_ascendingly_called_list(facultycalledcountdictionary= dict(),areaofinterest=dict(),teamarea=list(),exclude=list()):
    area_countfaculty_dic = dict()
    for fac in areaofinterest.keys():
        if fac not in exclude:
            for area in areaofinterest[fac]:
                if area in area_countfaculty_dic.keys():
                    area_countfaculty_dic[area].append((facultycalledcountdictionary[fac],fac))
                else:
                    area_countfaculty_dic[area] = list()
                    area_countfaculty_dic[area].append((facultycalledcountdictionary[fac],fac))

    for area in area_countfaculty_dic.keys():
        area_countfaculty_dic[area].sort()

    teamarea_faculty_ordered_list = list()
    for area in teamarea:
        for countfac in area_countfaculty_dic[area]:
            _,fac = countfac
            teamarea_faculty_ordered_list.append(fac)

    all_other_countfac_sorted_called_list = list()
    for area in area_countfaculty_dic.keys():
        if area not in teamarea:
            for countfac in area_countfaculty_dic[area]:
                all_other_countfac_sorted_called_list.append(countfac)
    all_other_countfac_sorted_called_list.sort()

    all_other_fac_ordered_list = list()
    for tup in all_other_countfac_sorted_called_list:
        _,fac = tup
        all_other_fac_ordered_list.append(fac)

    return teamarea_faculty_ordered_list+all_other_fac_ordered_list


