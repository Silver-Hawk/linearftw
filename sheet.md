
#exer 1


	min						77x1	+	70x2	+	88x3	+	84x4	+	94x5
	s.t.
	% of tin		60x1	+	25x2	+	45x3	+	20x4	+	50x5	>= 	40
	% of zinc	10x1	+	15x2	+	45x3	+	50x4	+	40x5	>= 	35
	% of lead	30x1	+	60x2	+	10x3	+	30x4	+	10x5	>= 	25

#exer 2

Let I be the set of cargos 1,..,4 indexed by i and J={Font,Center,Back} be the 
set of compartments indexed by j. Let x_ij be the variables representing the
amount of cargo i in compartment j
	
	w_i	= 	weight of cargo i
	v_i	= 	volume of cargo i	
	c_i	=	Cost of cargo i
	
	wc_j	= 	Weight capacity of compartment j
	vc_j	= 	Space capacity of compartment j	
	

	max sum_I sum_J (x_ij * c_i)
	s.t.
	sum_J sum_I x_ij *w_i <= wc_j
	sum_J sum_I x_ij *v_i <= vc_j
	
	(sum_I x_i1 * w_i/wc_1) - (sum_I x_i3 * w_i/wc_3) == 0 
	(sum_I x_i1 * w_i/wc_1) - (sum_I x_i2 * w_i/wc_2) == 0 

#exer 3

Mathematical Formulation

Let I be the set of classes {Y,B,M} indexed by i and J = {a,b,c} be the set of flights (chp->o,o->aa,chp->aa). 

Let x_ij be the variables representing the number of pasengers en class i on flight j

	tp_ij	=	ticket price for class i at flight j
	ub_ij =	upper bound on passengers in class i at flight j

	max sum_I sum_J x_ij * tp_ij 
	s.t.
	x_ij <= ub_ij 
 	sum_I x_i1 	+	x_i3 	<= 30
	sum_i xi2 	+ 	xi3 	<= 30

#Exer 4

	

