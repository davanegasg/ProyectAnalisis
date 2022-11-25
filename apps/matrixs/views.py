import json
from django.views.generic import TemplateView

from apps.matrixs.functions.Cholesky import fill_matrix
from apps.matrixs.functions.Crout import crout
from apps.matrixs.functions.Doolittle import doolittle
from apps.matrixs.functions.GaussSeidel import gaussSeidel
from apps.matrixs.functions.GaussianEliminationWithPartialPivoting import eliminacionParcial
from apps.matrixs.functions.GaussianEliminationWithTotalPivoting import eliminacionTotal
from apps.matrixs.functions.GaussianSimpleElimination import eliminacionSimple
from apps.matrixs.functions.Jacobi import jacobi
from apps.matrixs.functions.LUWithPartialPivoting import luParcial
from apps.matrixs.functions.LUwithGaussianSimpleElimination import luSimple
from apps.matrixs.functions.Sor import sor


def convert_string_to_list(string1):
    res = f"[{string1}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json


class CholeskyTemplateView(TemplateView):
    template_name = "matrixs/Cholesky.html"
    def get_context_data(self, **kwargs):
        context = super(CholeskyTemplateView,
                        self).get_context_data(**kwargs)

        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_a = self.request.GET.get('a', '')
        matrix_b = self.request.GET.get('b', '')  # [1],[1],[1],[1]

        if matrix_a and matrix_b:
            matrix_a = matrix_a
            matrix_b = matrix_b
            context["result"] = fill_matrix(matrix_a, matrix_b)[0]
            context["result_chol"] = fill_matrix(matrix_a, matrix_b)[1]
        return context


class CroutTemplateView(TemplateView):
    template_name = "matrixs/Crout.html"

    def get_context_data(self, **kwargs):
        context = super(CroutTemplateView,
                        self).get_context_data(**kwargs)

        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_a = self.request.GET.get('a', '')
        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_b = self.request.GET.get('b', '')

        if matrix_a and matrix_b:
            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)
            context["result"] = crout(matrix_a, matrix_b)

        return context


class DoolittleTemplateView(TemplateView):
    template_name = "matrixs/Doolittle.html"

    def get_context_data(self, **kwargs):
        context = super(DoolittleTemplateView,
                        self).get_context_data(**kwargs)

        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_a = self.request.GET.get('a', '')
        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_b = self.request.GET.get('b', '')

        if matrix_a and matrix_b:
            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)
            context["result"] = doolittle(matrix_a, matrix_b)

        return context


class GaussianEliminationWithPartialPivotingTemplateView(TemplateView):
    template_name = "matrixs/GaussianEliminationWithPartialPivoting.html"

    def get_context_data(self, **kwargs):
        context = super(GaussianEliminationWithPartialPivotingTemplateView,
                        self).get_context_data(**kwargs)

        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_a = self.request.GET.get('a', '')
        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_b = self.request.GET.get('b', '')

        if matrix_a and matrix_b:
            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)
            context["result"] = eliminacionParcial(matrix_a, matrix_b)

        return context


class GaussianEliminationWithTotalPivotingTemplateView(TemplateView):
    template_name = "matrixs/GaussianEliminationWithTotalPivoting.html"

    def get_context_data(self, **kwargs):
        context = super(GaussianEliminationWithTotalPivotingTemplateView,
                        self).get_context_data(**kwargs)

        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_a = self.request.GET.get('a', '')
        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_b = self.request.GET.get('b', '')

        if matrix_a and matrix_b:
            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)
            context["result"] = eliminacionTotal(matrix_a, matrix_b)

        return context


class GaussianSimpleEliminationTemplateView(TemplateView):
    template_name = "matrixs/GaussianSimpleElimination.html"

    def get_context_data(self, **kwargs):
        context = super(GaussianSimpleEliminationTemplateView,
                        self).get_context_data(**kwargs)

        # [2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]
        matrix_a = self.request.GET.get('a', '')
        matrix_b = self.request.GET.get('b', '')  # [1,1,1,1]

        if matrix_a and matrix_b:
            # [2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]
            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)  # 1,1,1,1
            context["result"] = eliminacionSimple(matrix_a, matrix_b)

        return context


class GaussSeidelTemplateView(TemplateView):
    template_name = "matrixs/GaussSeidel.html"

    def get_context_data(self, **kwargs):
        context = super(GaussSeidelTemplateView,
                        self).get_context_data(**kwargs)

        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_a = self.request.GET.get('A', '')
        matrix_b = self.request.GET.get('B', '')  # [1,1,1,1]
        matrix_x0 = self.request.GET.get('x0', '')  # [0,0,0,0]
        itermax = self.request.GET.get('itermax', '')  # 100
        tolerance = self.request.GET.get('tolerance', '')  # 0.00000007

        if matrix_a and matrix_b and matrix_x0 and itermax and tolerance:

            itermax = int(itermax)
            tolerance = float(tolerance)

            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)
            matrix_x0 = convert_string_to_list(matrix_x0)

            context["result"] = gaussSeidel(
                matrix_a, matrix_b, matrix_x0, itermax, tolerance)

        return context


class JacobiTemplateView(TemplateView):
    template_name = "matrixs/Jacobi.html"

    def get_context_data(self, **kwargs):
        context = super(JacobiTemplateView,
                        self).get_context_data(**kwargs)

        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_a = self.request.GET.get('A', '')
        matrix_b = self.request.GET.get('B', '')  # [1,1,1,1]
        matrix_x0 = self.request.GET.get('x0', '')  # [0,0,0,0]
        itermax = self.request.GET.get('itermax', '')  # 100
        tolerance = self.request.GET.get('tolerance', '')  # 0.00000007

        if matrix_a and matrix_b and matrix_x0 and itermax and tolerance:

            itermax = int(itermax)
            tolerance = float(tolerance)

            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)
            matrix_x0 = convert_string_to_list(matrix_x0)

            context["result"] = jacobi(
                matrix_a, matrix_b, matrix_x0, tolerance, itermax)

        return context


class LUwithGaussianSimpleEliminationTemplateView(TemplateView):
    template_name = "matrixs/LUwithGaussianSimpleElimination.html"

    def get_context_data(self, **kwargs):
        context = super(LUwithGaussianSimpleEliminationTemplateView,
                        self).get_context_data(**kwargs)

        # [2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]
        matrix_a = self.request.GET.get('a', '')
        matrix_b = self.request.GET.get('b', '')  # [1,1,1,1]

        if matrix_a and matrix_b:
            # [2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]
            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)  # 1,1,1,1
            context["result"] = luSimple(matrix_a, matrix_b)

        return context


class LUWithPartialPivotingTemplateView(TemplateView):
    template_name = "matrixs/LUWithPartialPivoting.html"

    def get_context_data(self, **kwargs):
        context = super(LUWithPartialPivotingTemplateView,
                        self).get_context_data(**kwargs)

        # [2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]
        matrix_a = self.request.GET.get('a', '')
        matrix_b = self.request.GET.get('b', '')  # [1,1,1,1]

        if matrix_a and matrix_b:
            # [2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]
            matrix_a = convert_string_to_list(matrix_a)
            matrix_b = convert_string_to_list(matrix_b)  # 1,1,1,1
            context["result"] = luParcial(matrix_a, matrix_b)

        return context


class SorTemplateView(TemplateView):
    template_name = "matrixs/Sor.html"

    def get_context_data(self, **kwargs):
        context = super(SorTemplateView,
                        self).get_context_data(**kwargs)

        # [4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]
        matrix_a = self.request.GET.get('A', '')
        matrix_b = convert_string_to_list(self.request.GET.get('B', ''))  # 1,1,1,1
        matrix_x0 = convert_string_to_list(self.request.GET.get('x0', ''))  # 0,0,0,0
        w = self.request.GET.get('w', '')  # [0,0,0,0]
        itermax = self.request.GET.get('itermax', '')  # 100
        tolerance = self.request.GET.get('tolerance', '')  # 0.00000007

        
        
        #A = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
        #b = [1, 1, 1, 1]
        #tol = 1e-7
        #w = 1.5
        #itermax = 20
        #sor(A,b,x0,Tol,w,Nmax)

        if matrix_a and matrix_b and matrix_x0 and w and itermax and tolerance:

            itermax = int(itermax)
            tolerance = float(tolerance)
            w = float(w)

            matrix_a = convert_string_to_list(matrix_a)
            
            print(type(matrix_a))
            print(type(matrix_b))
            print(type(matrix_x0))
            print(type(tolerance))
            print(type(w))
            print(type(itermax))

            context["result"] = sor(
                matrix_a, matrix_b, matrix_x0, tolerance, w, itermax
            )

        return context
