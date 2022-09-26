
class Secante{
	double x0, tol;
	int nIter;
	
	public static void main(String[] args){
		calculaRaiz();
	}
	
	static private double xnplus1(double x0, double x1){
        //NOTA xi = x1 y x = x0
		double fX0 = Math.pow(x0,2)-(2*x0)+2-Math.exp(x0); //Escribir la formula
        double fX1 = Math.pow(x1, 2)-(2*x1)+2-Math.exp(x1); //Escribir la formula
		double x2 = x1 - (fX1*(x1-x0))/(fX1-fX0); 
		return x2;
	}
	
	static public void calculaRaiz(){
		double x0 = 0.1, x1 = 0.6,tol = 1e-7, nIter = 20; //X0, Tolerancia, Iteraciones
		double x2 = xnplus1(x0, x1), n = 1;
		double error = Math.abs(x1-x0);
		System.out.println("It = 0   X = "+x0);
        System.out.println("It = 1   X = "+x1 + " Error = " + error);
		while(error>tol){
			n++; //Iteración +1
			x0 = x1; //X0
            x1 = x2;
			x2 = xnplus1(x0, x1); //X1
			if(n > nIter) break; //
			error = Math.abs(x1-x0); //Error
			System.out.println("It = "+n+" X = "+x1+" Xn+1 = "+x2+ " Error = " +error);
		}
		if(error<=tol){
			System.out.println(x1 + " es Secante con " + tol + " en it " + n);
		} else {
			System.out.println("No encontro solucion");
		}
		
	}
}