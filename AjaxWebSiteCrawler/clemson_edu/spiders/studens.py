# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.utils.url import urljoin_rfc
from scrapy import Item, Field
import json,string
class MyItem(Item):
    result=Field()
    url=Field()
    length=Field()
dept_codes=[    
{"expiration":"2014-10-02T10:06:09-0400","data":[{"id":"AAHN","name":"AAH Nondegree"},{"id":"AAH","name":"AAH Undeclared"},{"id":"ACCT","name":"Accounting"},{"id":"ADSU","name":"Admin and Supervision"},{"id":"AFLN","name":"AFLS Nondegree"},{"id":"AFLS","name":"AFLS Undeclared"},{"id":"AGRB","name":"Agribusiness"},{"id":"AAE","name":"Agric and Applied Econ"},{"id":"AGED","name":"Agricultural Education"},{"id":"AGME","name":"Agricultural Mech and Business"},{"id":"AVS","name":"Animal and Veterinary Sc"},{"id":"ANTH","name":"Anthropology"},{"id":"AES","name":"Applied Econ and Stat"},{"id":"APEC","name":"Applied Economics"},{"id":"AHRE","name":"Applied Hlth Res and Ev"},{"id":"APPS","name":"Applied Psychology"},{"id":"APSO","name":"Applied Sociology"},{"id":"AFWB","name":"Aqua, Fish, Wildlife Bio"},{"id":"ARCH","name":"Architecture"},{"id":"AUDT","name":"Audit"},{"id":"AUE","name":"Automotive Engineering"},{"id":"BBSN","name":"BBS Nondegree"},{"id":"BIMB","name":"Biochem and Molec Biol"},{"id":"BIOC","name":"Biochemistry"},{"id":"BIOE","name":"Bioengineering"},{"id":"BIOS","name":"Biological Sciences"},{"id":"BMED","name":"Biomedical Engineering"},{"id":"BIEN","name":"Biosystems Engineering"},{"id":"BUAD","name":"Business Administration"},{"id":"CTE","name":"Career and Tech Educ"},{"id":"CME","name":"Ceramic and Mat Engr"},{"id":"CHEN","name":"Chemical Engineering"},{"id":"CHEM","name":"Chemistry"},{"id":"CRP","name":"City and Reg Planning"},{"id":"CIVE","name":"Civil Engineering"},{"id":"CLIF","name":"Clemson LIFE"},{"id":"CHSR","name":"Clinic and Hlth Serv Res"},{"id":"CTS","name":"Communic, Tec and Soc"},{"id":"COMM","name":"Communication Studies"},{"id":"CPEN","name":"Computer Engineering"},{"id":"CIS","name":"Computer Info Systems"},{"id":"CPSC","name":"Computer Science"},{"id":"CSM","name":"Construction Sci and Mgt"},{"id":"COED","name":"Counselor Education"},{"id":"CURI","name":"Curriculum and Instr"},{"id":"DPA","name":"Digital Production Arts"},{"id":"ECHE","name":"Early Childhood Educ"},{"id":"ECON","name":"Economics"},{"id":"EDLE","name":"Educational Leadership"},{"id":"ELEN","name":"Electrical Engineering"},{"id":"ELED","name":"Elementary Education"},{"id":"ESE","name":"Engineering and Sci Educ"},{"id":"ENGR","name":"Engineering Undeclared"},{"id":"ENGL","name":"English"},{"id":"ESN","name":"Engr and Sci Nondegree"},{"id":"ENT","name":"Entomology"},{"id":"ENVE","name":"Environmental Engr"},{"id":"EES","name":"Environmental Engr\/Sci"},{"id":"ENTX","name":"Environmental Toxicology"},{"id":"ENR","name":"Environmental\/Nat Res"},{"id":"EVMG","name":"Event Management"},{"id":"FINM","name":"Financial Management"},{"id":"FDSC","name":"Food Science"},{"id":"FDTH","name":"Food Technology"},{"id":"FDNC","name":"Food, Nutr and Culin Sci"},{"id":"FORM","name":"Forest Resource Mgt"},{"id":"FORR","name":"Forest Resources"},{"id":"FSR","name":"Former Student Returning"},{"id":"GENG","name":"General Engineering"},{"id":"GEN","name":"Genetics"},{"id":"GEOL","name":"Geology"},{"id":"GCOM","name":"Graphic Communications"},{"id":"HLTH","name":"Health Science"},{"id":"HCG","name":"Healthcare Genetics"},{"id":"HEHN","name":"HEHD Nondegree"},{"id":"HEHD","name":"HEHD Undeclared"},{"id":"HP","name":"Historic Preservation"},{"id":"HIST","name":"History"},{"id":"HORT","name":"Horticulture"},{"id":"HCC","name":"Human Centered Computing"},{"id":"HFPS","name":"Human Factors Psychology"},{"id":"HRD","name":"Human Resource Dev"},{"id":"HYDR","name":"Hydrogeology"},{"id":"INEN","name":"Industrial Engineering"},{"id":"IOPS","name":"Industrial\/Organ Psych"},{"id":"IFCS","name":"Int Family and Comm Stu"},{"id":"IDND","name":"Interdiscipl Nondegree"},{"id":"INEX","name":"International Exchange"},{"id":"LARC","name":"Landscape Architecture"},{"id":"LIH","name":"Language and Inter Hlth"},{"id":"LIT","name":"Language and Inter Trade"},{"id":"LITR","name":"Literacy"},{"id":"MGT","name":"Management"},{"id":"MKT","name":"Marketing"},{"id":"MSE","name":"Materials Sci and Engr"},{"id":"MTHS","name":"Mathematical Sciences"},{"id":"MTCH","name":"Mathematics Teaching"},{"id":"ME","name":"Mechanical Engineering"},{"id":"MICR","name":"Microbiology"},{"id":"MLEV","name":"Middle-Level Education"},{"id":"MLAN","name":"Modern Languages"},{"id":"NURS","name":"Nursing"},{"id":"NUPM","name":"Nursing Postmasters"},{"id":"PKGS","name":"Packaging Science"},{"id":"PRTM","name":"Parks, Rec and Tour Mgt"},{"id":"PHIL","name":"Philosophy"},{"id":"PHOT","name":"Photonic Sci and Tech"},{"id":"PHYS","name":"Physics"},{"id":"PDBE","name":"Plan, Des and Built Env"},{"id":"PES","name":"Plant and Env Sciences"},{"id":"POST","name":"Policy Studies"},{"id":"POSC","name":"Political Science"},{"id":"PFC","name":"Polymer and Fiber Chem"},{"id":"PFSC","name":"Polymer and Fiber Sci"},{"id":"PREB","name":"Pre-Business"},{"id":"PRPH","name":"Prepharmacy"},{"id":"PPFH","name":"Preprof Health Studies"},{"id":"PPFS","name":"Preprofessional Studies"},{"id":"PREH","name":"Prerehabilitation Sci"},{"id":"PERF","name":"Prod Stu in Perform Arts"},{"id":"PROC","name":"Professional Comm"},{"id":"PSYC","name":"Psychology"},{"id":"PADM","name":"Public Administration"},{"id":"PUBM","name":"Public Management"},{"id":"RED","name":"Real Estate Development"},{"id":"RELS","name":"Religious Studies"},{"id":"RCID","name":"Rhet, Comm and Inf Des"},{"id":"RNGE","name":"RN General Education"},{"id":"STCH","name":"Science Teaching"},{"id":"SECE","name":"Secondary Education"},{"id":"SOC","name":"Sociology"},{"id":"SSCS","name":"Soils and Sust Crop Sys"},{"id":"SPED","name":"Special Education"},{"id":"SPEC","name":"Special Student"},{"id":"SPOC","name":"Sports Communication"},{"id":"SYSE","name":"Systems Engineering"},{"id":"TLRN","name":"Teaching and Learning"},{"id":"THRD","name":"Tech and Human Res Dev"},{"id":"TEXC","name":"Textile Chemistry"},{"id":"TRAN","name":"Transient"},{"id":"TURF","name":"Turfgrass"},{"id":"VART","name":"Visual Arts"},{"id":"VTED","name":"Vocational and Tech Educ"},{"id":"WFB","name":"Wildlife and Fish Biol"},{"id":"WOML","name":"Women's Leadership"},{"id":"YTHD","name":"Youth Develop Leadership"}],"size":6352}   ]
class PypiSpider(CrawlSpider):
    """
    We can use logger to log any messages like errors, debug or even info messages
    """
    url_counter=0
    count=0
    seen=set()
    name = "stu"
    allowed_domains = ["clemson.edu"]
    
    def _urljoin(self, response, url):
        """        takes url and response => converts into absolute url    """     
        return urljoin_rfc(response.url, url, response.encoding)            

    
    def start_requests(self,):
        
        #grab the home page.
        yield Request(url="https://my.clemson.edu/",callback=self.parse_students,)
    def parse_students(self,response):
        headers={}
        headers['Host']='my.clemson.edu'
        headers['Referer']='https://my.clemson.edu/'
        headers['User-Agent']='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:32.0) Gecko/20100101 Firefox/32.0'
        headers['X-Requested-With']="XMLHttpRequest"
        data=dept_codes[0]['data']
        codes=[i['id'] for i in data ]
        print codes
        combinations=[i+'*' for i in list(string.ascii_lowercase)]
        urls=[]
        for i in list(string.ascii_lowercase)+['',]:
            for j in list(string.ascii_lowercase)+['',]:
                for k in list(string.ascii_lowercase)+['',]:
                    combination=(i+j+k).strip()+"*"
                    if len(combination)!=4: print combination
                    url="https://my.clemson.edu/srv/feed/dynamic/directory/search?name="+combination
                    urls.append(url)
        print len(urls)
        urls=list(set(urls))
        print urls[0],urls[1],urls[2000]
        print len(urls) 
        for counter,url in enumerate(urls):
            #yield Request(url=url,callback=self.parse_student_info,headers=headers,meta={'dont_merge_cookies':True,'counter':counter},dont_filter=True)
            pass
    def parse_student_info(self,response):
         self.url_counter+=1
         item=MyItem()
         item['result']=response.body
         item['url']=response.url
         item['length']=len(json.loads(response.body))
         self.count+=item['length']
         yield item
         print "********************************************************"
         print self.count, item['length']
         print self.url_counter
         print "********************************************************"
