class BusquedaInc{
	public static void main(String[] args){
		calculaRaiz();
	}

	static public void calculaRaiz(){
      double x0 = 0, delta = 0, nIter = 20;
      double fX0 = x0; //PONER AQUÍ LA FORMULA
      if(fX0==0){
         print(x0+" Es raiz");
      } else{
         double x1 = x0+delta;
         int n = 1;
         double fX1 = x1; //PONER AQUÍ LA FORMULA
         while(fX0*fX1>0){
            if(n<nIter) break;
            x0 = x1;
            fX0 = fX1;
            x1 = x0+delta;
            fX1 = x1; //PONER AQUÍ LA FORMULA
            n++;
         }
         if(fX1==0) print(x1+" Es raiz");
         else if(fX0*fX1<0) print("Hay una raiz entre "+ x0+ " y " + x1);
         else print("Fracaso en " + nIter + " Iteraciones");
      }
   }

   static public void print(String x){
      System.out.println(x);
   }
}
