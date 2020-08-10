#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment,title,paragraph):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title,styles['h1'])
    white_space = Spacer(1,20)
    name_list=[]
    weight_list=[]
    for each_dict in paragraph:
        name_list.append("name: {}".format(each_dict['name']))
        weight_list.append("weight: {} lbs".format(each_dict['weight']))
    a,b,c,d,e,f,g,h,i,j=[name_list[i] for i in (0,1,2,3,4,5,6,7,8,9)]
    k,l,m,n,o,p,q,r,s,t=[weight_list[i] for i in (0,1,2,3,4,5,6,7,8,9)]
    report_a=Paragraph(a,styles['BodyText'])
    report_k=Paragraph(k,styles['BodyText'])
    report_b=Paragraph(b,styles['BodyText'])
    report_l=Paragraph(l,styles['BodyText'])
    report_c=Paragraph(c,styles['BodyText'])
    report_m=Paragraph(m,styles['BodyText'])
    report_d=Paragraph(d,styles['BodyText'])
    report_n=Paragraph(n,styles['BodyText'])
    report_e=Paragraph(e,styles['BodyText'])
    report_o=Paragraph(o,styles['BodyText'])
    report_f=Paragraph(f,styles['BodyText'])
    report_p=Paragraph(p,styles['BodyText'])
    report_g=Paragraph(g,styles['BodyText'])
    report_q=Paragraph(q,styles['BodyText'])
    report_h=Paragraph(h,styles['BodyText'])
    report_r=Paragraph(r,styles['BodyText'])
    report_i=Paragraph(i,styles['BodyText'])
    report_s=Paragraph(s,styles['BodyText'])
    report_j=Paragraph(j,styles['BodyText'])
    report_t=Paragraph(t,styles['BodyText'])
    print(a,k,'\n',
        b,l,'\n',
        c,m,'\n',
        d,n,'\n',
        e,o,'\n',
        f,p,'\n',
        g,q,'\n',
        h,r,'\n',
        i,s,'\n',
        j,t)
    report.build([report_title,
                white_space,
                report_a,report_k,
                white_space,
                report_b,report_l,
                white_space,
                report_c,report_m,
                white_space,
                report_d,report_n,
                white_space,
                report_e,report_o,
                white_space,
                report_f,report_p,
                white_space,
                report_g,report_q,
                white_space,
                report_h,report_r,
                white_space,
                report_i,report_s,
                white_space,
                report_j,report_t])
