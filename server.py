import cherrypy
import oauth2
import requests
import pymysql
import subprocess
from lxml import etree
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

class HelloWorld(object):
    
    #affichage de la page d'accueil HTML
    def index(self):
        tmpl = env.get_template("index.html")
        return tmpl.render()
    index.exposed = True
    
    "Chargement depuis index.html des critères de recherche
    def php_tmpl(self, **param):
        tmpl = env.get_template("index-test.php")
        return tmpl.render()
    php_tmpl.exposed = True

    def xml(self):
        tmpl = env.get_template("xml.html")
        return tmpl.render()
    xml.exposed = True
    
    #Fonction pour la génération du fichier XML
    def ajout(self, ville, categorie):
        consumer_key    = 'eYaJtTiUJlSKpOgIrMDwrg'
        consumer_secret = 'Fv0JTznlgg9ulRgf_YFjoJ4q2VU'
        token           = 'Ah4uL-IH2Lf6vGpUORnmlqcOacTEHLP4'
        token_secret    = 'swK6ERX4OyKDRIvo_EbGK45JSZ0'

        consumer = oauth2.Consumer(consumer_key, consumer_secret)

        category_filter = categorie
        print(category_filter)
        location = ville
        print(location)
        options =  'category_filter=%s&location=%s&sort=1' % (category_filter, location)
        url = 'http://api.yelp.com/v2/search?' + options

        oauth_request = oauth2.Request('GET', url, {})
        oauth_request.update({'oauth_nonce'      : oauth2.generate_nonce(),
                      'oauth_timestamp'  : oauth2.generate_timestamp(),
                      'oauth_token'       : token,
                      'oauth_consumer_key': consumer_key})

        token = oauth2.Token(token, token_secret)
        oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
        signed_url = oauth_request.to_url()

        resp = requests.get(url=signed_url)
        Points_interets = resp.json()

        id = 1
        chaine = []
        
        #Récupréation des informations recherchées depuis l'API
        for business in Points_interets['businesses']:
            i = str(id)
            name = business['name']
            n = str(name)
            rating = business['rating']
            r = str(rating)
            review = business['review_count']
            re = str(review)
            latitude = business['location']['coordinate']['latitude']
            la = str(latitude)
            longitude = business['location']['coordinate']['longitude']
            lo = str(longitude)
            city = business['location']['city']
            c = str(city)
            id = id+1
            tup = (i, n, r, re, la, lo, c, category_filter),
            chaine += tup
        print(chaine)

        businessesd = etree.Element("businesses")

        buinesses_data = chaine
        
        #Création de l'arborescence XML
        for buiness_data in buinesses_data:
            busi = etree.SubElement(businessesd, "businesses")
            busi.set("data-id", buiness_data[0])
            nom = etree.SubElement(busi, "name")
            nom.text = buiness_data[1]
            vote = etree.SubElement(busi, "rating")
            vote.text = buiness_data[2]
            nb_avis = etree.SubElement(busi, "review_count")
            nb_avis.text = buiness_data[3]
            lat = etree.SubElement(busi, "latitude")
            lat.text = buiness_data[4]
            long = etree.SubElement(busi, "longitude")
            long.text = buiness_data[5]
            cit = etree.SubElement(busi, "city")
            cit.text = buiness_data[6]
            cat = etree.SubElement(busi, "category")
            cat.text = category_filter
        tree = businessesd.getroottree()
        tree.write('api.xml')
        tmpl = env.get_template("affxml.html")
        return tmpl.render()
    ajout.exposed = True

    def api_bdd(self, categorie, ville):
        consumer_key    = 'eYaJtTiUJlSKpOgIrMDwrg'
        consumer_secret = 'Fv0JTznlgg9ulRgf_YFjoJ4q2VU'
        token           = 'Ah4uL-IH2Lf6vGpUORnmlqcOacTEHLP4'
        token_secret    = 'swK6ERX4OyKDRIvo_EbGK45JSZ0'
        
        #Connexion à la base de données
        db = pymysql.connect (host='localhost',
                      user='root',
                      password='',
                      database='stiv')
        cur = db.cursor()

        consumer = oauth2.Consumer(consumer_key, consumer_secret)

        category_filter = categorie
        catego = str(category_filter)
        location = ville
        options =  'category_filter=%s&location=%s&sort=1' % (category_filter, location)
        url = 'http://api.yelp.com/v2/search?' + options

        oauth_request = oauth2.Request('GET', url, {})
        oauth_request.update({'oauth_nonce'      : oauth2.generate_nonce(),
                      'oauth_timestamp'  : oauth2.generate_timestamp(),
                      'oauth_token'       : token,
                      'oauth_consumer_key': consumer_key})

        token = oauth2.Token(token, token_secret)
        oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
        signed_url = oauth_request.to_url()

        resp = requests.get(url=signed_url)
        Points_interets = resp.json()

        #Insertion des donées dans la base de donées
        for business in Points_interets['businesses']:

            cur.execute('INSERT INTO test(id, rating, name, review_count, latitude, longitude, city) VALUES (NULL, {}, "{}", {}, {}, {}, "{}")'.format(business['rating'], business['name'], business['review_count'], business['location']['coordinate']['latitude'], business['location']['coordinate']['longitude'], business['location']['city']))
            db.commit()
            cur.execute("UPDATE test SET category='"+catego+"' WHERE latitude = {}".format(business['location']['coordinate']['latitude']))
            db.commit()
            

#Chargement des données dans la BDD
HelloWorld.api_bdd(HelloWorld(),'restaurants','Paris, FR')
HelloWorld.api_bdd(HelloWorld(),'shopping','Paris, FR')
HelloWorld.api_bdd(HelloWorld(),'restaurants','Marseille, FR')
HelloWorld.api_bdd(HelloWorld(),'shopping','Marseille, FR')
#Lancement Cherrypy
cherrypy.quickstart(HelloWorld(), config='server.conf')

