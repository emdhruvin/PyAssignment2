from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c=canvas.Canvas("20CE143_Sem3_Result.pdf")

c.setFont('Times-Roman',32)
c.drawString(30,770,'CHARUSAT')

c.setFontSize(6.2)
c.drawString(30,760,'CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY')

c.setFont('Helvetica-Bold',12)
c.drawString(220,782,'CHAROTAR UNIVERSITY OF SCIENCE AND TECHNOLOGY')
# for font in c.getAvailableFonts():
#     print(font)

c.setFont('Helvetica',8.8)
c.drawString(220,770,'CHARUSAT Campus, Changa - 388421 , Off Nadiad - Petlad Highway, Gujarat (India)')
c.drawString(220,760,'Ph. # +91-2697-265001,265021 Fax. # +91-2697-265007')
c.drawString(220,750,'Web : www.charusat.ac.in | Email : info@charusat.ac.in')
c.drawString(100,730,'(Formed under Gujarat State Act No. 8 of 2009, and degreed conferred u/s 22 of UGC Act. 1956)')
c.drawString(220,720,'(Accredited with Grade \'A\' by NAAC)')

c.setFont('Helvetica-Bold',18)
c.drawString(175,700,'SEMESTER GRADE REPORT')
c.setFont('Helvetica-Bold',16)
c.drawString(106,670,'FACULTY OF TECHNOLOGY AND ENGINEERING')

c.setFont('Times-Roman',14)
c.drawString(30,640,'No. : Q8419')
c.drawString(430,640,'Date : 19/03/2022')
c.drawString(30,620,'Name : TANDEL DHRUVIN ARUNKUMAR')
c.drawString(30,600,'Programme : B.TECH.(COMPUTER)')
c.drawString(430,600,'ID.No. : 20CE143')
c.drawString(30,580,'Month & Year : November 2021')
c.drawString(280,580,'Semester : 3')
c.drawString(430,580,'Aadhar : 776749597230')

c.drawString(220,540,'Course')

c.drawString(30,520,'CE244')#for sgp
c.drawString(100,520,'SOWFTWARE GROUP PROJECT-I')#for sgp
c.drawString(320,520,'PRACTICAL')#for sgp

c.drawString(30,500,'CE251')#for java
c.drawString(100,500,'JAVA PROGRAMMING')#for java
c.drawString(320,500,'THEORY')#for java
c.drawString(320,480,'PRACTICAL')#for java

c.drawString(30,460,'CE252')#for DE
c.drawString(100,460,'DIGITAL ELECTRONICS')#forDE
c.drawString(320,460,'THEORY')#for DE
c.drawString(320,440,'PRACTICAL')#for DE

c.drawString(30,420,'CE257')#for DCN
c.drawString(100,420,'DATA COMMUNICATION')#DCN
c.drawString(320,420,'THEORY')#for DCN
c.drawString(100,400,' & NETWORK')
c.drawString(320,400,'PRACTICAL')#for DCN

c.drawString(30,380,'HS121.02A')#for HS
c.drawString(100,380,'CREATIVIY, PROBLEM SOLVING')#for HS
c.drawString(100,360,'AND INOVATION')
c.drawString(320,380,'PRACTICAL')#for HS

c.drawString(30,340,'IT281.01')#for IT
c.drawString(100,340,'ICT RESOURCES & MULTIMEDIA')#IT
c.drawString(320,340,'PRACTICAL')#for IT

c.drawString(30,320,'MA253')#for MATH
c.drawString(100,320,'DISCRETE MATHAMATICS')#for MATH
c.drawString(100,300,'AND ALGEBRA')
c.drawString(320,320,'THEORY')#for MATH

c.drawString(420,540,'Credit')

c.drawString(425,520,'2.00')#for sgp

c.drawString(425,500,'3.00')#for JAVA
c.drawString(425,480,'2.00')#for JAVA

c.drawString(425,460,'3.00')#for DE
c.drawString(425,440,'1.00')#for DE

c.drawString(425,420,'4.00')#for DCN
c.drawString(425,400,'1.00')#for DCN

c.drawString(425,380,'2.00')#for HS

c.drawString(425,340,'2.00')#for IT

c.drawString(425,320,'4.00')#for MATH

c.drawString(500,540,'Grade')

c.drawString(510,520,'AA')#for sgp

c.drawString(510,500,'BC')#for java
c.drawString(510,480,'AA')#for JAVA

c.drawString(510,460,'AB')#for DE
c.drawString(510,440,'BC')#for DE

c.drawString(510,420,'AA')#for DCN
c.drawString(510,400,'AA')#for DCN

c.drawString(510,380,'AA')#for HS

c.drawString(510,340,'AA')#for IT

c.drawString(510,320,'AA')#for MA

c.drawString(90,270,'Semester Performance')
c.drawString(30,250,'Total Credits')
c.drawString(50,230,'24.00')
c.drawString(120,250,'Credit Earned')
c.drawString(140,230,'24.00')
c.drawString(210,250,'SGPA')
c.drawString(215,230,'9.38')

c.drawString(320,270,'Cumilative Performance')
c.drawString(260,250,'Total Credits')
c.drawString(280,230,'61.00')
c.drawString(350,250,'Credit Earned')
c.drawString(370,230,'61.00')
c.drawString(440,250,'CGPA')
c.drawString(445,230,'9.28')

c.drawString(515,270,'Class')
c.drawString(500,240,'Distinction')

c.drawString(30,200,'Previous SGPA : 9.32')
c.drawString(230,200,'Previous CGPA : 9.22')
c.drawString(420,200,'No. of BackLog : 0')

c.setFont('Helvetica',24)
c.drawString(450,160,'Sign')
c.setFont('Times-Roman',14)
c.drawString(448,145,'Registrar')

c.setFont('Helvetica',9)
c.drawString(240,180,'EX/REG/CE/NT/2/21/148')

c.setFont('Helvetica',7)
c.drawString(210,50,'NB : infringement / tamperinfg of this document is legal offence')
c.drawString(500,50,'Details overleaf')
c.save()
