"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from jk.sitemap import IdeesSitemap,SportSitemap,CultureSitemap,EconomieSitemap,EditorialSitemap,NationalSitemap,SanteSitemap,SocieteSitemap,TicketmagSitemap
from jk.sitemap import NewsSitemap,PoliticsSitemap,BusinessSitemap,HealthSitemap,OpinionSitemap,TechSitemap,ScienceSitemap
from django.contrib.sitemaps import views
idees = {
    'idees':IdeesSitemap,

}
sport ={
    'sport': SportSitemap,
}
culture = {
    'culture':CultureSitemap,
}
economie = {
    'economie':EconomieSitemap,
}
editorial = {
    'editorial':EditorialSitemap,
}
national = {
    'national':NationalSitemap,
}
sante = {
    'sante':SanteSitemap,
}
societe = {
    'societe':SocieteSitemap,
}
ticketmag = {
    'ticketmag':TicketmagSitemap,
}

news = {
    'news':NewsSitemap,
}
politics = {
    'politics':PoliticsSitemap,
}
business = {
    'business':BusinessSitemap,
}

opinion = {
    'opinion':OpinionSitemap,
}
tech = {
    'tech':TechSitemap,
}
science = {
    'science':ScienceSitemap,
}

health = {
    'health':HealthSitemap,
}
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('jk.urls')),
    #url(r'^search/', include('haystack.urls')),
    url(r'^idees/sitemap.xml$', views.sitemap, {'sitemaps': idees}),
    url(r'^sport/sitemap.xml$', views.sitemap, {'sitemaps': sport}),
    url(r'^culture/sitemap.xml$', views.sitemap, {'sitemaps': culture}),
    url(r'^economie/sitemap.xml$', views.sitemap, {'sitemaps': economie}),
    url(r'^editorial/sitemap.xml$', views.sitemap, {'sitemaps': editorial}),
    url(r'^national/sitemap.xml$', views.sitemap, {'sitemaps': national}),
    url(r'^sante/sitemap.xml$', views.sitemap, {'sitemaps': sante}),
    url(r'^societe/sitemap.xml$', views.sitemap, {'sitemaps': societe}),
    url(r'^ticketmag/sitemap.xml$', views.sitemap, {'sitemaps': ticketmag}),

    url(r'^en/news/sitemap.xml$', views.sitemap, {'sitemaps': news}),
    url(r'^en/politics/sitemap.xml$', views.sitemap, {'sitemaps': politics}),
    url(r'^en/business/sitemap.xml$', views.sitemap, {'sitemaps': business}),

    url(r'^en/opinion/sitemap.xml$', views.sitemap, {'sitemaps': opinion}),
    url(r'^en/tech/sitemap.xml$', views.sitemap, {'sitemaps': tech}),
    url(r'^en/science/sitemap.xml$', views.sitemap, {'sitemaps': science}),

    url(r'^en/health/sitemap.xml$', views.sitemap, {'sitemaps': health}),


]
