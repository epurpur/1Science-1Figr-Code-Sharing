#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:03:39 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches
from operator import itemgetter
import numpy as np



def number_of_papers_published_per_year():
    """Plots # of papers published by all big 5 providers per year"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    papers_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        papers_by_year = []
        
        total_2008 = subset_by_provider.total_2008.tolist()
        papers_by_year.append(total_2008[0])
        total_2009 = subset_by_provider.total_2009.tolist()
        papers_by_year.append(total_2009[0])
        total_2010 = subset_by_provider.total_2010.tolist()
        papers_by_year.append(total_2010[0])
        total_2011 = subset_by_provider.total_2011.tolist()
        papers_by_year.append(total_2011[0])
        total_2012 = subset_by_provider.total_2012.tolist()
        papers_by_year.append(total_2012[0])
        total_2013 = subset_by_provider.total_2013.tolist()
        papers_by_year.append(total_2013[0])
        total_2014 = subset_by_provider.total_2014.tolist()
        papers_by_year.append(total_2014[0])
        total_2015 = subset_by_provider.total_2015.tolist()
        papers_by_year.append(total_2015[0])
        total_2016 = subset_by_provider.total_2016.tolist()
        papers_by_year.append(total_2016[0])
        total_2017 = subset_by_provider.total_2017.tolist()
        papers_by_year.append(total_2017[0])

        papers_by_provider.append(papers_by_year)        
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Number of Total Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Paper Count')
    
    plt.plot(years, papers_by_provider[0], label='Elsevier')
    plt.plot(years, papers_by_provider[1], label='Sage')
    plt.plot(years, papers_by_provider[2], label='Springer')
    plt.plot(years, papers_by_provider[3], label='Taylor & Francis')
    plt.plot(years, papers_by_provider[4], label='Wiley')
    
    plt.legend()
    
#    plt.show()
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def number_papers_over_time():
    """Plots # of authored publications at your institution in each of the big 5 providers over time (2008-2017)
    Looks at columns under 'Papers per journal/provider by your institution's authors"""

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    publications_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        publications_by_year = []
        
        papers_2008 = subset_by_provider.papers_2008.tolist()
        publications_by_year.append(papers_2008[0])
        papers_2009 = subset_by_provider.papers_2009.tolist()
        publications_by_year.append(papers_2009[0])
        papers_2010 = subset_by_provider.papers_2010.tolist()
        publications_by_year.append(papers_2010[0])
        papers_2011 = subset_by_provider.papers_2011.tolist()
        publications_by_year.append(papers_2011[0])
        papers_2012 = subset_by_provider.papers_2012.tolist()
        publications_by_year.append(papers_2012[0])
        papers_2013 = subset_by_provider.papers_2013.tolist()
        publications_by_year.append(papers_2013[0])
        papers_2014 = subset_by_provider.papers_2014.tolist()
        publications_by_year.append(papers_2014[0])
        papers_2015 = subset_by_provider.papers_2015.tolist()
        publications_by_year.append(papers_2015[0])
        papers_2016 = subset_by_provider.papers_2016.tolist()
        publications_by_year.append(papers_2016[0])
        papers_2017 = subset_by_provider.papers_2017.tolist()
        publications_by_year.append(papers_2017[0])
        
        publications_by_provider.append(publications_by_year)
            
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Number of UVA Authored Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Paper Count')

    #change this to be dynamic instead of hard coded
    plt.plot(years, publications_by_provider[0], label='Elsevier')
    plt.plot(years, publications_by_provider[1], label='Sage')
    plt.plot(years, publications_by_provider[2], label='Springer')
    plt.plot(years, publications_by_provider[3], label='Taylor & Francis')
    plt.plot(years, publications_by_provider[4], label='Wiley')
    
    plt.legend()

#    plt.show()    
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def oa_percent_papers_available_over_time():
    """Percent of papers available Open Access (oa) for each of the big 5 providers over time (2008-2017)
    Looks at columns under '% of OA papers in 1findr per journal/provider (intersection with Scopus)"""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    oa_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        oa_by_year = []

        oa_2008 = subset_by_provider.oa_2008.tolist()
        oa_by_year.append(oa_2008[0])
        oa_2009 = subset_by_provider.oa_2009.tolist()
        oa_by_year.append(oa_2009[0])
        oa_2010 = subset_by_provider.oa_2010.tolist()
        oa_by_year.append(oa_2010[0])
        oa_2011 = subset_by_provider.oa_2011.tolist()
        oa_by_year.append(oa_2011[0])
        oa_2012 = subset_by_provider.oa_2012.tolist()
        oa_by_year.append(oa_2012[0])
        oa_2013 = subset_by_provider.oa_2013.tolist()
        oa_by_year.append(oa_2013[0])
        oa_2014 = subset_by_provider.oa_2014.tolist()
        oa_by_year.append(oa_2014[0])
        oa_2015 = subset_by_provider.oa_2015.tolist()
        oa_by_year.append(oa_2015[0])
        oa_2016 = subset_by_provider.oa_2016.tolist()
        oa_by_year.append(oa_2016[0])
        oa_2017 = subset_by_provider.oa_2017.tolist()
        oa_by_year.append(oa_2017[0])
        
        oa_by_provider.append(oa_by_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
        
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percentage of OA Available Papers by Year in 2017 by Provider')
    plt.xlabel('Year')
    plt.ylabel('Percent Papers Available')
    plt.ylim(0, .45)
    
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    plt.plot(years, oa_by_provider[0], label='Elsevier')
    plt.plot(years, oa_by_provider[1], label='Sage')
    plt.plot(years, oa_by_provider[2], label='Springer')
    plt.plot(years, oa_by_provider[3], label='Taylor & Francis')
    plt.plot(years, oa_by_provider[4], label='Wiley')
    
    plt.legend()

#    plt.show()    
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def big5_percent_jr5_of_jr1():
    """A measurement of currency. Compares JR5 downloads to JR1 downloads for each of the big 5 providers.
    JR5 downloads are 2017 articles downloaded in 2017.
    JR1 downloads are all years articles downloaded in 2017.
    We want to see what % of current articles people are downloading."""
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    percent_jr5_of_jr1 = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr1_total = i[2]
                jr5_total = i[3]
                ratio = jr5_total/jr1_total
                percent_jr5_of_jr1.append(ratio)
                
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent JR5 downloads of JR1 downloads (for 2017)')
    plot = plt.bar(big5, percent_jr5_of_jr1, width=.8, color='green')   
    plt.ylabel('Percent of Total')
    plt.ylim(0, 1)  #changes top and bottom limit of y axis in plot

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    
    for i in plot:
        score = i.get_height()
        
        plt.text(i.get_x() + i.get_width()/2., 
                 1.05 * score, 
                 '{:.1%}'.format(score),
                 ha='center',
                 va='bottom')

#    plt.show()        
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def references_over_time():
    """Your institution's references by provider by year, referencing Scopus data.
    Looks at columns under 'References to journal/provider by your institution's authors (as measured in Scopus)
    References are defined as: Number of References made by researchers of your institution to an article from a given journal"""
    

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    ref_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        ref_by_year = []
    
        ref_2008 = subset_by_provider.ref_2008.tolist()
        ref_by_year.append(ref_2008[0])
        ref_2009 = subset_by_provider.ref_2009.tolist()
        ref_by_year.append(ref_2009[0])
        ref_2010 = subset_by_provider.ref_2010.tolist()
        ref_by_year.append(ref_2010[0])
        ref_2011 = subset_by_provider.ref_2011.tolist()
        ref_by_year.append(ref_2011[0])
        ref_2012 = subset_by_provider.ref_2012.tolist()
        ref_by_year.append(ref_2012[0])
        ref_2013 = subset_by_provider.ref_2013.tolist()
        ref_by_year.append(ref_2013[0])
        ref_2014 = subset_by_provider.ref_2014.tolist()
        ref_by_year.append(ref_2014[0])
        ref_2015 = subset_by_provider.ref_2015.tolist()
        ref_by_year.append(ref_2015[0])
        ref_2016 = subset_by_provider.ref_2016.tolist()
        ref_by_year.append(ref_2016[0])
        ref_2017 = subset_by_provider.ref_2017.tolist()
        ref_by_year.append(ref_2017[0])
        
        ref_by_provider.append(ref_by_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of References Made by UVA Researchers by Provider')
    plt.xlabel('Year')
    plt.ylabel('Number References')
    plt.ylim(0, 18000)

    plt.plot(years, ref_by_provider[0], label='Elsevier')
    plt.plot(years, ref_by_provider[1], label='Sage')
    plt.plot(years, ref_by_provider[2], label='Springer')
    plt.plot(years, ref_by_provider[3], label='Taylor & Francis')
    plt.plot(years, ref_by_provider[4], label='Wiley')

    plt.legend()  

#    plt.show()    
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def jr1_big5_jr80_jr90_jr95_stacked_bar():
    """Creates stacked bar plot showing jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of your institution's jr1 downloads. JR90 are journals that make up 90% of your institution's jr1 downloads.
    JR95 are journals that make up 95% of your institution's jr1 downloads. These will all be plotted together."""
    
#    TODO: ADD LABELS TO PLOT
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)


    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 
        
    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr1_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr1_downloads += i[2]
            total_journals += 1
            
        jr1_tuples = [(i[0], i[2]) for i in journals_data]
        jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr1_tuples

        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in jr1_tuples_sorted:
            if jr80_running_tally < (total_jr1_downloads * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
#                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
#                
        for i in jr1_tuples_sorted:
            if jr90_running_tally < (total_jr1_downloads * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)


        for i in jr1_tuples_sorted:
            if jr95_running_tally < (total_jr1_downloads * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles Downloaded by Provider (JR1 Downloads)')
    plt.ylabel('Percent of total titles')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %
    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')

#    plt.show()        
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def jr5_big5_jr80_jr90_jr95_stacked_bar():
    """Creates stacked bar plot showing jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of your insitution's jr5 downloads. JR90 are journals that make up 90% of your institution's jr5 downloads.
    JR95 are journals that make up 95% of your institution's jr5 downloads. These will all be plotted together."""

#    TODO: ADD LABELS TO PLOT

    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 

    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr5_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr5_downloads += i[3]
            total_journals += 1
            
        jr5_tuples = [(i[0], i[3]) for i in journals_data]
        jr5_tuples_sorted = sorted(jr5_tuples, key = lambda i: i[1], reverse=True)     #sorts on second element of jr1_tuples
        
        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in jr5_tuples_sorted:
            if jr80_running_tally < (total_jr5_downloads * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
                
        for i in jr5_tuples_sorted:
            if jr90_running_tally < (total_jr5_downloads * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)

        for i in jr5_tuples_sorted:
            if jr95_running_tally < (total_jr5_downloads * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        print(total_journals)
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles Downloaded by Provider (JR5 Downloads)')
    plt.ylabel('Percent of total titles')
    
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')

#    plt.show()
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def references_big5_jr80_jr90_jr95_stacked_bar():
    """Creates stacked bar plot showing jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of your institution's references. JR90 are journals that make up 90% of your institution's references.
    JR95 are journals that make up 95% of your institution's references. These will all be plotted together."""


#    TODO: ADD LABELS TO PLOT

    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)           


    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 
#    big5 = ['AIP']        
    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_references = 0
        total_journals = 0                         
        for i in journals_data:
            total_references += i[4]
            total_journals += 1
            
        reference_tuples = [(i[0], i[4]) for i in journals_data]
        reference_tuples_sorted = sorted(reference_tuples, key = lambda i: i[1], reverse=True)     #sorts on second element of jr1_tuples
        
        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in reference_tuples_sorted:
            if jr80_running_tally < (total_references * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
                
        for i in reference_tuples_sorted:
            if jr90_running_tally < (total_references * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)

        for i in reference_tuples_sorted:
            if jr95_running_tally < (total_references * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        print(total_journals)
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles Referenced by Provider')
    plt.ylabel('Percent of total titles')
    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')
        
#    plt.show()
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def papers_big5_jr80_jr90_jr95_stacked_bar():
    """Creates stacked bar plot showing jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of your institution's papers. JR90 are journals that make up 90% of your institution's papers.
    JR95 are journals that make up 95% of your insitution's papers. These will all be plotted together."""


#    TODO: ADD LABELS TO PLOT

    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)           


    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 
#    big5 = ['AIP']        
    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_papers = 0
        total_journals = 0                         
        for i in journals_data:
            total_papers += i[5]
            total_journals += 1
            
        paper_tuples = [(i[0], i[5]) for i in journals_data]
        paper_tuples_sorted = sorted(paper_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr1_tuples
        
        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in paper_tuples_sorted:
            if jr80_running_tally < (total_papers * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
                
        for i in paper_tuples_sorted:
            if jr90_running_tally < (total_papers * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)

        for i in paper_tuples_sorted:
            if jr95_running_tally < (total_papers * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        print(total_journals)
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles with Papers by UVA Authors')
    plt.ylabel('Percent of total titles')
    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')

#    plt.show()
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def total_references_per_year():
    """Total references by provider by year, referencing Scopus data.
    Looks at columns under 'References to journal/provider by your institution's authors (as measured in Scopus)
    References are defined as: Number of References made by researchers of your institution to an article from a given journal"""
    

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    providers = ['Wiley', 'U Chicago Press', 'Taylor & Francis', 'Springer', 'Sage', 'SPIE', 'Royal Society of Chemistry', 'Project MUSE',
                 'ProQuest', 'Oxford UP', 'Ovid', 'Modern Language Association', 'MIT Press', 'Karger', 'JSTOR', 'IOPscience', 'IEEE', 'Gale',
                 'Emerald', 'Elsevier', 'Ebsco', 'DeGruyter', 'Cambridge UP', 'Brill', 'BioOne', 'Association for Computing Machinery', 'Annual Reviews',
                 'American Society of Mechanical Engineers', 'American Society of Civil Engineers', 'American Physical Society', 'American Mathematical Society',
                 'American Institute of Aeronautics and Astronautics', 'American Chemical Society', 'AIP']
                 
    sum_2008 = 0
    sum_2009 = 0
    sum_2010 = 0
    sum_2011 = 0
    sum_2012 = 0
    sum_2013 = 0
    sum_2014 = 0
    sum_2015 = 0
    sum_2016 = 0
    sum_2017 = 0
    
    for provider_name in providers:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        ref_2008 = subset_by_provider.ref_2008.tolist()
        sum_2008 += ref_2008[0]
        ref_2009 = subset_by_provider.ref_2009.tolist()
        sum_2009 += ref_2009[0]
        ref_2010 = subset_by_provider.ref_2010.tolist()
        sum_2010 += ref_2010[0]
        ref_2011 = subset_by_provider.ref_2011.tolist()
        sum_2011 += ref_2011[0]
        ref_2012 = subset_by_provider.ref_2012.tolist()
        sum_2012 += ref_2012[0]
        ref_2013 = subset_by_provider.ref_2013.tolist()
        sum_2013 += ref_2013[0]
        ref_2014 = subset_by_provider.ref_2014.tolist()
        sum_2014 += ref_2014[0]
        ref_2015 = subset_by_provider.ref_2015.tolist()
        sum_2015 += ref_2015[0]
        ref_2016 = subset_by_provider.ref_2016.tolist()
        sum_2016 += ref_2016[0]
        ref_2017 = subset_by_provider.ref_2017.tolist()
        sum_2017 += ref_2017[0]
        
    totals_by_year = list((sum_2008, sum_2009, sum_2010, sum_2011, sum_2012, sum_2013, sum_2014, sum_2015, sum_2016, sum_2017))
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of References Made by UVA Researchers \n (across all providers)')
    plt.xlabel('Year')
    plt.ylabel('Number References')
    plt.ylim(0, 120000)

    plt.plot(years, totals_by_year)

#    plt.show()    
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory

