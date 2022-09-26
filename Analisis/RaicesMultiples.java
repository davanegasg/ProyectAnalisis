class RaicesMultiples{
	double x0, tol;
	int nIter;
	
	public static void main(String[] args){
		calculaRaiz();
	}
	
	static private double xnplus1(double x){
		double fx = Math.pow(x, 3)-5*Math.pow(x,2)+7*x-3; //Escribir la formula
		double fDerivada = 3*Math.pow(x, 2)-10*x+7; //Escribir la derivada de la formula
        double f2Derivada = 6*x-10;
		double y = x - (fx*fDerivada)/(Math.pow(fDerivada, 2)-(fx*f2Derivada)); 
		return y;
	}
	
	static public void calculaRaiz(){
		double x0 = 0, tol = 1e-20, nIter = 20; //X0, Tolerancia, Iteraciones
		double x1 = xnplus1(x0), n = 0;
		int n2 = 1;
		double error = Math.abs(x1-x0);
		System.out.println("It = 0   X = "+x0+" Error1 = " + error);
		while(error>tol){
			n++; //Iteración +1
			n2++;
			x0 = x1; //X0
			x1 = xnplus1(x0); //X1
			if(n > nIter) break; //
			error = Math.abs(x1-x0); //Error
			System.out.println("It = "+n+" X = "+x0+" Xn+1 = "+x1+ " Error" +n2+" = " +error);
		}
		if(error<=tol){
			System.out.println(x1 + " es Newton con " + tol + " en it " + n);
		} else {
			System.out.println("No encontro solucion");
		}
		
	}
}
