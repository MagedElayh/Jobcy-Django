from django.views.generic import TemplateView

# Jobs
class JobList(TemplateView):
    template_name = "pages/jobs/job-list.html"
class JobList2(TemplateView):
    template_name = "pages/jobs/job-list-2.html"
class JobGrid(TemplateView):
    template_name = "pages/jobs/job-grid.html"
class JobGrid2(TemplateView):
    template_name = "pages/jobs/job-grid-2.html"
class JobDetails(TemplateView):
    template_name = "pages/jobs/job-details.html"
class JobCategories(TemplateView):
    template_name = "pages/jobs/job-categories.html"

# Candidates-Company
class CandidateList(TemplateView):
    template_name = "pages/candidates-company/candidate-list.html"
class CandidateGrid(TemplateView):
    template_name = "pages/candidates-company/candidate-grid.html"
class CandidateDetails(TemplateView):
    template_name = "pages/candidates-company/candidate-details.html"
class CompanyList(TemplateView):
    template_name = "pages/candidates-company/company-list.html"
class CompanyDetails(TemplateView):
    template_name = "pages/candidates-company/company-details.html"

# Extra-Pages
class SignUp(TemplateView):
    template_name = "pages/extra-pages/sign-up.html"
class Signin(TemplateView):
    template_name = "pages/extra-pages/sign-in.html"
class SignOut(TemplateView):
    template_name = "pages/extra-pages/sign-out.html"
class ResetPassword(TemplateView):
    template_name = "pages/extra-pages/reset-password.html"
class ComingSoon(TemplateView):
    template_name = "pages/extra-pages/coming-soon.html"
class Error404(TemplateView):
    template_name = "pages/extra-pages/404-error.html"
class Components(TemplateView):
    template_name = "pages/extra-pages/components.html"