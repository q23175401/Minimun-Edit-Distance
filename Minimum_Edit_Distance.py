import numpy as np

DELETE_COST = 1
INSERT_COST = 1
SUBSTITUDE_COST = 2
LEAVE_COST = 0

def MED(ori_s, new_s):
    dist_mat = np.empty([len(ori_s), len(new_s)], dtype = object)
    action_mat = np.empty([len(ori_s), len(new_s)], dtype = object)

    med, action_string = MED_re(ori_s, new_s, 0, 0, dist_mat, action_mat)
    return med, action_string   # return the med and one of the aciton string that can change ori_s to new_s

def MED_re(ori_s, new_s, ori_s_index, new_s_index, dist_mat, action_mat):
    if len(ori_s)-ori_s_index == 0:
        insert_string = ""
        for a in range(new_s_index, len(new_s)):
            insert_string += "<ins_({})> ".format(new_s[a])
        return (len(new_s)-new_s_index) * INSERT_COST, insert_string
    elif len(new_s)-new_s_index == 0:
        delete_string = ""
        for a in range(ori_s_index, len(ori_s)):
            delete_string = "<del_({})> ".format(ori_s[a])
        return (len(ori_s)-ori_s_index) * DELETE_COST, delete_string

    if dist_mat[ori_s_index, new_s_index] != None:
        return dist_mat[ori_s_index, new_s_index], action_mat[ori_s_index, new_s_index]

    delete_cost, d_action = MED_re(ori_s, new_s, ori_s_index+1, new_s_index, dist_mat, action_mat)   # delete
    delete_cost += DELETE_COST          # delete action

    insert_cost, i_action = MED_re(ori_s, new_s, ori_s_index, new_s_index+1, dist_mat, action_mat)   # insert
    insert_cost += INSERT_COST          # insert action

    if ori_s[ori_s_index] == new_s[new_s_index]:    # they are the same, leave the character
        replace_cost = LEAVE_COST       # leave action take
    else:
        replace_cost = SUBSTITUDE_COST  # substitution action

    replace_or_leave_cost, re_action = MED_re(ori_s, new_s, ori_s_index+1, new_s_index+1, dist_mat, action_mat)
    replace_or_leave_cost += replace_cost

    if (delete_cost <= insert_cost and delete_cost <= replace_or_leave_cost):  # when delete action cost the least
        action_string = "<del_({})> ".format(ori_s[ori_s_index]) + d_action
        med = delete_cost
    elif insert_cost < delete_cost and insert_cost <= replace_or_leave_cost:   # when insert action cost the least
        action_string = "<ins_({})> ".format(new_s[new_s_index]) + i_action
        med = insert_cost
    elif replace_or_leave_cost < insert_cost and replace_or_leave_cost < delete_cost:  # when replace or leave action cost the least
        if replace_cost == LEAVE_COST:   # leave the original character
            action_string = "<lea_({})> ".format(ori_s[ori_s_index]) + re_action
        else:                            # replace the original character to the new one
            action_string = "<sub_({})_({})> ".format(ori_s[ori_s_index], new_s[new_s_index]) + re_action
        med = replace_or_leave_cost

    dist_mat[ori_s_index, new_s_index] = med
    action_mat[ori_s_index, new_s_index] = action_string
    return med, action_string

def take_action(ori_s, action_string):     # The original sentence can take action to change to the new sentence
    actions = action_string.split()
    result = ""
    si = 0
    for action in actions:
        if action.find("del") != -1:
            si += 1
        elif action.find("ins") != -1:
            word = action[action.find("(")+1 : action.find(")")]
            result += word
        elif action.find("lea") != -1:
            word = ori_s[si]
            si += 1
            result += word
        elif action.find("sub") != -1:
            word = action[-3:-2]
            si += 1
            result += word
    return result

if __name__=="__main__":
    #ori_s = "123123123sdasdlahsdlkas12312sdsldkfhald3123"
    ori_s = "bbb"
    new_s = "7123812731237sd5123567534u900%^$&*f456ssfadad3s2d1f812935"

    med, action_string  = MED(ori_s, new_s)
    print(med)
    print(len(action_string.strip(' ').split(' ')))
    print(take_action(ori_s, action_string))
    print(new_s)
    
    
