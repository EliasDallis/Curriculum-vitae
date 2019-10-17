from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, DetailView, ListView
from helloworld import models, forms
# Create your views here.
# def index(request):
#     dictionary1 = {
#         'paragraph_text' : "Views contains a function with a dictionary, and returns render(request, XXX.html, context='the_dictionary'", 
#         'paragraph_text2' : "This is text from views.py going through the index.html template. The html contains double curly brackets {{}} referencing this dictionary key",
#         'paragraph_text3' : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ac lacus lacus. Nam nec sagittis lorem. In hac habitasse platea dictumst. Morbi lobortis eros justo, rhoncus elementum risus vulputate id. Morbi sem libero, dignissim a risus non, bibendum scelerisque nisi. Curabitur at rutrum tellus. Curabitur mattis imperdiet mi sit amet interdum. Cras iaculis nulla felis, pulvinar lacinia nisi laoreet ac. Donec in orci vel arcu iaculis ultrices. Phasellus mattis interdum diam id viverra. Etiam interdum dui sagittis augue pretium, id aliquet felis blandit. Nam ac rhoncus velit, dictum suscipit sem. Fusce dictum orci nec iaculis suscipit. Proin a enim vel odio laoreet sollicitudin. Sed mollis eget neque a aliquet. Etiam vitae sollicitudin ligula. Ut nec velit lorem. Vestibulum lacinia scelerisque odio. Duis pretium placerat purus, in faucibus eros sollicitudin feugiat. Aenean ullamcorper vestibulum nisi. Donec vel odio odio. Donec felis elit, iaculis eu interdum a, lobortis et ipsum. Proin sagittis malesuada quam id congue. Cras et mollis eros. Mauris tincidunt urna blandit mi sodales aliquam. Pellentesque feugiat odio sed ligula euismod dignissim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque dapibus orci libero, eget elementum nisi auctor in. Maecenas varius mauris id diam pretium, et efficitur turpis vulputate. Suspendisse ultrices nisl sit amet est finibus, nec facilisis nibh fermentum. Etiam semper pharetra justo vel efficitur. Duis eget auctor orci, vel auctor ante. Fusce id lectus interdum, consectetur velit eget, consequat lectus. Nullam porta convallis diam non tempus. Curabitur sollicitudin, enim eu auctor hendrerit, enim odio ultricies odio, ac vehicula metus ante non felis. Sed ut tincidunt ante. Quisque vitae augue at tellus luctus interdum et id turpis. Nullam interdum accumsan lacinia. Ut non suscipit arcu. Vivamus velit nulla, consequat sit amet justo id, varius tempor dui. Phasellus dui eros, efficitur id malesuada egestas, egestas id urna. Nullam ex est, varius in bibendum sed, pellentesque non mauris. Etiam sit amet nulla at ante egestas pretium. Mauris iaculis eu arcu sit amet tincidunt. Nam ornare sapien efficitur, consectetur ipsum ac, commodo elit. Ut porttitor posuere ligula non pretium. Proin volutpat venenatis elit, id dapibus ex auctor sed. Donec lectus quam, vestibulum et lectus sit amet, pellentesque convallis lorem. Nam vel egestas mi. Nam sit amet tellus rhoncus, cursus dui eu, aliquam turpis."
#         }
#     return render(request, 'index.html', context=dictionary1)

class IndexView(TemplateView):
    template_name = 'index.html'

# class CVView(TemplateView):
#     template_name = 'CV.html'

# class BioView(TemplateView):
#     template_name = 'helloworld/bio.html'

class PortfolioView(ListView):
    template_name = 'helloworld/portfolio.html'
    model = models.Portfolio
    context_object_name = 'portfolioitems'

class PreviousFirmView(ListView):
    context_object_name = 'previousfirms'
    model = models.PreviousTitle
    template_name = 'helloworld/previous.html'

class BioView(ListView):
    context_object_name = 'biolist'
    model = models.Biography
    template_name = 'helloworld/bio.html'

# class EducationView(ListView):
#     # Works - templates need key from ctx  
#     ##!!!context_object_name = 'previouscourses'
#     model = models.Education
#     ####template_name = 'helloworld/previous_2.html'   ##defaults to [model name]_list.html
#     def get_context_data(self, **kwargs):
#         ctx = super(EducationView, self).get_context_data(**kwargs)
#         ctx['previouscourses'] = models.Education.objects.all()
#         ctx['skill'] = models.Skill.objects.all()
#         return ctx

class EducationView(ListView):
    model = models.Education
    template_name = 'helloworld/education_list.html'

    def previouscourses(self):
        return models.Education.objects.all()

    def skill(self):
        print('hello from skill ctx function')
        return models.Skill.objects.all()

# class SkillView(ListView):
#     context_object_name = 'skills'
#     model = models.Skill


class PreviousTitleView(DetailView):
    context_object_name = 'previousjobs'
    model = models.PreviousTitle
    template_name = 'helloworld/CV_all.html'

class DownloadView(TemplateView):
    template_name = 'helloworld/cv_download.html'

def ContactOne(request):
    form = forms.ContactForm()
    

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            customer = (form.cleaned_data['name'])
            names = customer.split()
            first_name = names[0]
            return render(request, 'helloworld/contact_thanks.html', {'customer':first_name})

            # print("Post received and validated")
            # print(form.cleaned_data['name'])
            # customer = (form.cleaned_data['name'])
            # print(form.cleaned_data['email'])
            # print(form.cleaned_data['text'])
            # return render(request, 'helloworld/contact_thanks.html', {'customer':customer})

            
    
    return render(request, 'helloworld/contact_form.html', {'form':form})