import solution

sol = solution.Solution()

assert sol.solve("1,2<A>00") == "1,2100"
assert sol.solve("<B>12,1") == "112,1"
assert sol.solve("12,1<A>,2<B>,3<C>") == "12,112,2112,32112"
assert sol.solve("1<B>,2<C>,3<D>,44") == "12344,2344,344,44"
assert sol.solve("1<B>,2<D>,3<A>,44") == "1244,244,31244,44"
assert sol.solve("12,1<C>,2<D>,3<A>") == "12,12312,2312,312"

assert sol.solve("") == ""
assert sol.solve("A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z") == "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
assert sol.solve("<A>,<B>,<C>") == "-1"
assert sol.solve("<B>,2<C>,3<A>") == "-1"
assert sol.solve("1,C<D>,F") == "-1"
assert sol.solve("1,C<D<A,F") == "-1"
assert sol.solve("1,CD>A,F") == "-1"
assert sol.solve("1,C<D><B>,F") == "-1"


print("All test cases passed!")