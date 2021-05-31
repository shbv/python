"""
Function arguments:
- required arguments
- positional arguments (optional): *args 
- keyword arguments (optional): **kwargs
"""
def func(req_arg, *args, **kwargs):
    print(req_arg)
    if args: print(args) # tuple
    if kwargs: print(kwargs) # dictionary

func('t_req')
print()
func('t_req', 't_opt1', 't_opt2')
print()
func('t_req', t_kw_opt1='t_kw_val1', t_kw_opt2='t_kw_val2')
print()
func('t_req', 't_opt1', 't_opt2', t_kw_opt1='t_kw_val1', t_kw_opt2='t_kw_val2' )
