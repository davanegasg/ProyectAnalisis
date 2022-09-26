class Biseccion{
	public static void main(String[] args){
		calculaRaiz();
	}

	static public void calculaRaiz(){
		double xI = 3, xF = 3.5, tol = 1e-8,xM = 0, fM = 0, error = 0; //X0, Tolerancia, Iteraciones
      double fXi = Math.pow(xI, 3)-7.51*Math.pow(xI, 2)+18.4239*xI-14.8331; //Cambiar esta función por la que nos entreguen
      double fXf = Math.pow(xF, 3)-7.51*Math.pow(xF, 2)+18.4239*xF-14.8331; //Cambiar esta función por la que nos entreguen
      
      if(fXi==0){
         print(xI + " Raiz");
      } else if (fXf==0){
         print(xF + " Raiz");
      } else if (fXi*fXf >0){
         print("Intervalo no valido");
      } else {
         xM = (xI+xF)/2;
         fM = Math.pow(xM, 3)-7.51*Math.pow(xM, 2)+18.4239*xM-14.8331; //Cambiar esta función por la que nos entreguen
         error = Math.abs(xF-xM);
         while(error>tol && fM!=0){
            if(fXi*fM<0){
               xF = xM;
               fXf = fM;
            } else {
               xI = xM;
               fXi = fM;
            }
            xM = (xI+xF)/2;
            fM = Math.pow(xM, 3)-7.51*Math.pow(xM, 2)+18.4239*xM-14.8331; //Cambiar esta función por la que nos entreguen
            error = Math.abs(xF-xM);
         }
      if(fM == 0){
         print(xM+" Raiz");
      } else {
         print(xM+" Raiz con tol = " + tol);
      }
      }
	}

   static public void print(String x){
      System.out.println(x);
   }
}
