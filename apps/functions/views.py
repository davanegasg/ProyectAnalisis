from django.views.generic import TemplateView

from apps.functions.functions.bisection import bisection
from apps.functions.functions.incrementalsearch import incrementalsearch
from apps.functions.functions.falserule import false_position
from apps.functions.functions.newton import newton
from apps.functions.functions.fixedpoint import fixed_point
from apps.functions.functions.secant import secant
from apps.functions.functions.multipleroots import multipleroot, dfun, d2fun


class IncrementalSearchTemplateView(TemplateView):
    template_name = "functions/incremental_search.html"

    def get_context_data(self, **kwargs):
        context = super(IncrementalSearchTemplateView,
                        self).get_context_data(**kwargs)

        function = self.request.GET.get('f', '').replace("^", "**")
        x0 = self.request.GET.get('x0', '')
        delta = self.request.GET.get('delta', '')
        itermax = self.request.GET.get('itermax', '')

        if function and x0 and delta and itermax:
            x0 = float(x0)
            delta = float(delta)
            itermax = int(itermax)

            functionresult = incrementalsearch(function, x0, delta, itermax)

            context['result'] = f"{functionresult}"

        return context


class BisectionTemplateView(TemplateView):
    template_name = "functions/bisection.html"

    def get_context_data(self, **kwargs):
        context = super(BisectionTemplateView,
                        self).get_context_data(**kwargs)

        function = self.request.GET.get('f', '').replace("^", "**")
        a = self.request.GET.get('a', '')
        b = self.request.GET.get('b', '')
        tol = self.request.GET.get('tol', '')
        n = self.request.GET.get('n', '')

        if function and a and b and tol and n:
            a = float(a)
            b = float(b)
            tol = float(tol)
            n = int(n)

            result = bisection(function, a, b, tol, n)[0]
            result_table = bisection(function, a, b, tol, n)[1]

            context['result'] = f"{result}"
            context['result_table'] = f"{result_table}"
        return context


class FalseRuleTemplateView(TemplateView):
    template_name = "functions/false_rule.html"

    def get_context_data(self, **kwargs):
        context = super(FalseRuleTemplateView,
                        self).get_context_data(**kwargs)

        function = self.request.GET.get('f', '').replace("^", "**")
        a = self.request.GET.get('a', '')
        b = self.request.GET.get('b', '')
        tol = self.request.GET.get('tol', '')
        n = self.request.GET.get('n', '')

        if function and a and b and tol and n:
            a = float(a)
            b = float(b)
            tol = float(tol)
            n = int(n)

            functionresult = false_position(function, a, b, tol, n)

            context['result'] = f"{functionresult}"

        return context


class NewtonTemplateView(TemplateView):
    template_name = "functions/newton.html"

    def get_context_data(self, **kwargs):
        context = super(NewtonTemplateView,
                        self).get_context_data(**kwargs)

        function = self.request.GET.get('f', '').replace("^", "**")
        p_0 = self.request.GET.get('p_0', '')
        tol = self.request.GET.get('tol', '')
        n = self.request.GET.get('n', '')

        if function and p_0 and tol and n:
            p_0 = float(p_0)
            tol = float(tol)
            n = int(n)

            n_dict = newton(function, p_0, tol, n)

            result = n_dict["solution"]
            result_table = n_dict["table"]
            xi = n_dict["xi"]
            fxi = n_dict["f(xi)"]

            context['f'] = self.request.GET.get('f', '').replace("^", "**")
            context['df'] = dfun(function, p_0)[1]
            context['result'] = f"{result}"
            context['result_table'] = f"{result_table}"
            context['xi'] = xi
            context['fxi'] = fxi

        return context


class FixedPointTemplateView(TemplateView):
    template_name = "functions/fixed_point.html"

    def get_context_data(self, **kwargs):
        context = super(FixedPointTemplateView,
                        self).get_context_data(**kwargs)

        g = self.request.GET.get('g', '').replace("^", "**")
        f1 = self.request.GET.get('f1', '').replace("^", "**")
        x0 = self.request.GET.get('x0', '')
        tol = self.request.GET.get('tol', '')
        itermax = self.request.GET.get('itermax', '')

        if g and f1 and x0 and tol and itermax:
            x0 = float(x0)
            tol = float(tol)
            itermax = int(itermax)

            result = fixed_point(g, f1, x0, tol, itermax)

            context['result_table'] = f"{result}"
        return context


class SecantTemplateView(TemplateView):
    template_name = "functions/secant.html"

    def get_context_data(self, **kwargs):
        context = super(SecantTemplateView,
                        self).get_context_data(**kwargs)

        function = self.request.GET.get('f', '').replace("^", "**")
        p_0 = self.request.GET.get('p_0', '')
        p_1 = self.request.GET.get('p_1', '')
        tol = self.request.GET.get('tol', '')
        n = self.request.GET.get('n', '')

        if function and p_0 and p_1 and tol and n:
            p_0 = float(p_0)
            p_1 = float(p_1)
            tol = float(tol)
            n = int(n)

            result = secant(function, p_0, p_1, tol, n)[0]
            result_table = secant(function, p_0, p_1, tol, n)[1]
            print(result)
            print()
            print(result_table)
            context['result'] = f"{result}"
            context['result_table'] = f"{result_table}"
        return context


class MultipleRootsTemplateView(TemplateView):
    template_name = "functions/multiple_roots.html"

    def get_context_data(self, **kwargs):
        context = super(MultipleRootsTemplateView,
                        self).get_context_data(**kwargs)

        function = self.request.GET.get('f', '').replace("^", "**")
        x0 = self.request.GET.get('x0', '')
        tol = self.request.GET.get('tol', '')
        n = self.request.GET.get('n', '')

        if function and x0 and tol and n:
            x0 = float(x0)
            tol = float(tol)
            n = int(n)

            result = multipleroot(function, x0, tol, n)[0]
            result_table = multipleroot(function, x0, tol, n)[1]

            context['f'] = function
            context['df'] = dfun(function, x0)[1]
            context['d2f'] = d2fun(function, x0)[1]
            context['result'] = f"{result}"
            context['result_table'] = f"{result_table}"
        return context
