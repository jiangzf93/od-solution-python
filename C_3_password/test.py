import solution

cases = [
    ['AB_3dccaa+', 'AB_3dccaa+,true'],
    ['AB_D3c', 'AB_D3c,false'],
    ['Ab+ddcca__', 'Ab+ddcca__,false'],
    ['DIEP323D__++', 'DIEP323D__++,false'],
    ['aa__dd3495', 'aa__dd3495,false'],
    ['abdc34dED3sefa', 'abdc34dED3sefa,false'],
    ['daokD<DF238<9__', 'daokDF239__,true'],
    ['dijf<<oD33<4E&&a', 'dioD34E&&a,true'],
    ['ad<fa9D<_d23', 'afa9_d23,false'],
    ['adfai3<Dfdafi*&', 'adfaiDfdafi*&,false'],
    ['fsi3Dda_<ad&<', 'fsi3Ddaad,false'],
    ['aa<D93F_+', 'aD93F_+,false'],
]

errors = []
for c in range(len(cases)):
    case = cases[c]
    sol = solution.Solution()
    if sol.solve(case[0]) != case[1]:
        errors.append(str(c))

if len(errors) > 0:
    print('error numbers:' + ', '.join(errors))
else:
    print('all passed!')