## app.py ######################################################################
## central app file containing a main function #################################
## I still think a lot like C ##################################################
################################################################################

from vector import vector_III;


def main():
	v1 = vector_III(1, 1, 1);
	v2 = vector_III(-1, 1, -1);
	print "dot product of (1,1,1) & (-1,1,-1) is " + str(v1.Dot(v2));
	return 0;
	
main();
