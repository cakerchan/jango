from django.contrib.sitemaps import Sitemap
from jk.models import Content,Contenten

class IdeesSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='idees',datime='2017-12-21')
    def categorylocation(self,obj):
        return 'idees'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)

class SportSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='sport',datime='2017-12-20')
    def categorylocation(self,obj):
        return 'sport'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class CultureSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='culture',datime='2017-12-19')
    def categorylocation(self,obj):
        return 'culture'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class EconomieSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='economie',datime='2018-01-08')
    def categorylocation(self,obj):
        return 'economie'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class EditorialSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='editorial',datime='2017-12-21')
    def categorylocation(self,obj):
        return 'editorial'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class NationalSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='national',datime='2017-12-21')
    def categorylocation(self,obj):
        return 'national'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class SanteSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='sante',datime='2017-12-13')
    def categorylocation(self,obj):
        return 'sante'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class SocieteSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='societe',datime='2017-12-21')
    def categorylocation(self,obj):
        return 'societe'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class TicketmagSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Content.objects.all().filter(category='ticketmag',datime='2017-12-13')
    def categorylocation(self,obj):
        return 'ticketmag'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)

class NewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Contenten.objects.all().filter(category='news',datime='2018-01-17')
    def categorylocation(self,obj):
        return 'news'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class PoliticsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Contenten.objects.all().filter(category='politics',datime='2018-01-10')
    def categorylocation(self,obj):
        return 'politics'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
class BusinessSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Contenten.objects.all().filter(category='business',datime='2018-01-10')
    def categorylocation(self,obj):
        return 'business'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)

class OpinionSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Contenten.objects.all().filter(category='opinion',datime='2018-01-22')
    def categorylocation(self,obj):
        return 'opinion'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)

class TechSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Contenten.objects.all().filter(category='tech',datime='2018-01-23')
    def categorylocation(self,obj):
        return 'tech'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)

class ScienceSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Contenten.objects.all().filter(category='science',datime='2018-01-23')
    def categorylocation(self,obj):
        return 'science'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)

class HealthSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.4

    def items(self):
        return Contenten.objects.all().filter(category='health',datime='2018-01-10')
    def categorylocation(self,obj):
        return 'health'
    def productslocation(self, obj):
        return '%s-%s' % (obj.title,obj.id)
