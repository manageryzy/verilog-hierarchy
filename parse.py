#!/usr/bin/python3
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re


def parse_instances(test_str: str):
    res = []
    regex = r"\b(?!always)(?!and)(?!assign)(?!automatic)(?!begin)(?!buf)(?!bufif0)(?!bufif1)(?!case)(?!casex)(?!casez)(?!cell)(?!cmos)(?!config)(?!deassign)(?!default)(?!defparam)(?!design)(?!disable)(?!edge)(?!else)(?!end)(?!endcase)(?!endconfig)(?!endfunction)(?!endgenerate)(?!endmodule)(?!endprimitive)(?!endspecify)(?!endtable)(?!endtask)(?!event)(?!for)(?!force)(?!forever)(?!fork)(?!function)(?!generate)(?!genvar)(?!highz0)(?!highz1)(?!if)(?!ifnone)(?!incdir)(?!include)(?!initial)(?!inout)(?!input)(?!instance)(?!integer)(?!join)(?!large)(?!liblist)(?!library)(?!localparam)(?!macromodule)(?!medium)(?!module)(?!nand)(?!negedge)(?!nmos)(?!nor)(?!noshowcancelledno)(?!not)(?!notif0)(?!notif1)(?!or)(?!output)(?!parameter)(?!pmos)(?!posedge)(?!primitive)(?!pull0)(?!pull1)(?!pulldown)(?!pullup)(?!pulsestyle_oneventglitch)(?!pulsestyle_ondetectglitch)(?!remos)(?!real)(?!realtime)(?!reg)(?!release)(?!repeat)(?!rnmos)(?!rpmos)(?!rtran)(?!rtranif0)(?!rtranif1)(?!scalared)(?!showcancelled)(?!signed)(?!small)(?!specify)(?!specparam)(?!strong0)(?!strong1)(?!supply0)(?!supply1)(?!table)(?!task)(?!time)(?!tran)(?!tranif0)(?!tranif1)(?!tri)(?!tri0)(?!tri1)(?!triand)(?!trior)(?!trireg)(?!unsigned)(?!use)(?!vectored)(?!wait)(?!wand)(?!weak0)(?!weak1)(?!while)(?!wire)(?!wor)(?!xnor)(?!xor)([a-zA-Z_][\w_]*)\s+(#\s*\([^;]*?\)){0,1}\s*(?!always)(?!and)(?!assign)(?!automatic)(?!begin)(?!buf)(?!bufif0)(?!bufif1)(?!case)(?!casex)(?!casez)(?!cell)(?!cmos)(?!config)(?!deassign)(?!default)(?!defparam)(?!design)(?!disable)(?!edge)(?!else)(?!end)(?!endcase)(?!endconfig)(?!endfunction)(?!endgenerate)(?!endmodule)(?!endprimitive)(?!endspecify)(?!endtable)(?!endtask)(?!event)(?!for)(?!force)(?!forever)(?!fork)(?!function)(?!generate)(?!genvar)(?!highz0)(?!highz1)(?!if)(?!ifnone)(?!incdir)(?!include)(?!initial)(?!inout)(?!input)(?!instance)(?!integer)(?!join)(?!large)(?!liblist)(?!library)(?!localparam)(?!macromodule)(?!medium)(?!module)(?!nand)(?!negedge)(?!nmos)(?!nor)(?!noshowcancelledno)(?!not)(?!notif0)(?!notif1)(?!or)(?!output)(?!parameter)(?!pmos)(?!posedge)(?!primitive)(?!pull0)(?!pull1)(?!pulldown)(?!pullup)(?!pulsestyle_oneventglitch)(?!pulsestyle_ondetectglitch)(?!remos)(?!real)(?!realtime)(?!reg)(?!release)(?!repeat)(?!rnmos)(?!rpmos)(?!rtran)(?!rtranif0)(?!rtranif1)(?!scalared)(?!showcancelled)(?!signed)(?!small)(?!specify)(?!specparam)(?!strong0)(?!strong1)(?!supply0)(?!supply1)(?!table)(?!task)(?!time)(?!tran)(?!tranif0)(?!tranif1)(?!tri)(?!tri0)(?!tri1)(?!triand)(?!trior)(?!trireg)(?!unsigned)(?!use)(?!vectored)(?!wait)(?!wand)(?!weak0)(?!weak1)(?!while)(?!wire)(?!wor)(?!xnor)(?!xor)([a-zA-Z_][\w_]*)\s*(\[[\s\S]*?\])*\s*(\([^;]*?\));"
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        res.append((match.group(), []))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            res[-1][1].append(match.group(groupNum))
    return res


def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " "  # note: a space and not an empty string
        else:
            return s

    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)


def parse_module(test_str: str):
    res = []
    regex = r"\bmodule\s+(?!always)(?!and)(?!assign)(?!automatic)(?!begin)(?!buf)(?!bufif0)(?!bufif1)(?!case)(?!casex)(?!casez)(?!cell)(?!cmos)(?!config)(?!deassign)(?!default)(?!defparam)(?!design)(?!disable)(?!edge)(?!else)(?!end)(?!endcase)(?!endconfig)(?!endfunction)(?!endgenerate)(?!endmodule)(?!endprimitive)(?!endspecify)(?!endtable)(?!endtask)(?!event)(?!for)(?!force)(?!forever)(?!fork)(?!function)(?!generate)(?!genvar)(?!highz0)(?!highz1)(?!if)(?!ifnone)(?!incdir)(?!include)(?!initial)(?!inout)(?!input)(?!instance)(?!integer)(?!join)(?!large)(?!liblist)(?!library)(?!localparam)(?!macromodule)(?!medium)(?!module)(?!nand)(?!negedge)(?!nmos)(?!nor)(?!noshowcancelledno)(?!not)(?!notif0)(?!notif1)(?!or)(?!output)(?!parameter)(?!pmos)(?!posedge)(?!primitive)(?!pull0)(?!pull1)(?!pulldown)(?!pullup)(?!pulsestyle_oneventglitch)(?!pulsestyle_ondetectglitch)(?!remos)(?!real)(?!realtime)(?!reg)(?!release)(?!repeat)(?!rnmos)(?!rpmos)(?!rtran)(?!rtranif0)(?!rtranif1)(?!scalared)(?!showcancelled)(?!signed)(?!small)(?!specify)(?!specparam)(?!strong0)(?!strong1)(?!supply0)(?!supply1)(?!table)(?!task)(?!time)(?!tran)(?!tranif0)(?!tranif1)(?!tri)(?!tri0)(?!tri1)(?!triand)(?!trior)(?!trireg)(?!unsigned)(?!use)(?!vectored)(?!wait)(?!wand)(?!weak0)(?!weak1)(?!while)(?!wire)(?!wor)(?!xnor)(?!xor)([a-zA-Z_][\w_]*)\s*(#\s*\([^;]*?\))*\s*(\([^;]*?\))\s*;([\s\S]*?)endmodule"
    matches = re.finditer(regex, test_str, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        res.append((match.group(), []))
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            res[-1][1].append(match.group(groupNum))
    return res


def parse_string(test_str: str):
    def transform_instances(input: list):
        o = {}
        for i in input:
            obj = {'raw': i[0], 'module': i[1][0], 'param': i[1][1], 'name': i[1][2], 'array': i[1][3],
                   'signals': i[1][4]}
            o[obj['name']] = obj
        return o

    res = {}
    test_str = comment_remover(test_str)
    modules = parse_module(test_str)
    for module in modules:
        o = {'raw': module[0], 'name': module[1][0], 'param': module[1][1], 'signals': module[1][2],
             'body': module[1][3]}
        o['instances'] = transform_instances(parse_instances(o['body']))
        res[module[1][0]] = o
    return res


def parse_file(file: str):
    with open(file) as f:
        data = "".join(f.readlines())
        f.close()
        return parse_string(data)


def parse_dir(path:str):
    def merge_two_dicts(x, y):
        z = x.copy()  # start with x's keys and values
        z.update(y)  # modifies z with y's keys and values & returns None
        return z
    import os
    res = {}
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            fname = os.path.join(root,file)
            if fname.endswith('.sv') or fname.endswith('.v'):
                file_info = parse_file(fname)
                res = merge_two_dicts(res, file_info)
    return res


if __name__ == '__main__':
    s = '''
    module A # (parameter pa) (input wire clk,//asd
    input wire rst,//asd
    asd ai);//asd
    B #(.pb(asd)) b [1:0] (//asd
    .clk(clk),//asd
    .rst(rst));//asd
    endmodule//asd


    module B #(parameter pb) (
       input logic clk,
       input logic rst);
       FFF fa();
     endmodule
    '''
    res = parse_string(s)



    pass
