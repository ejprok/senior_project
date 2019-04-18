from django.shortcuts import render

# Create your views here.


"""
Function get_sorted_blog_list 

#returns list of dictionaries - a number of blogs sorted by publish date
                a single featured blog will in the first 
                possition if relevant

blog_listing [{
        'author'       : "Jared Amalong",
        'pub_date'     : "Dec 31, 1992",
        'header_image" : one_image_URL,
        'body_images"  : list_of_images,
        'body"         : "text with <> anchors for images",
        'MediumURL"    : "https://medium.com/@amalong/hacking-education-d4047e5d5a29",
    },{
        'author'       : "Jared Amalong",
        'pub_date'     : "Jan 01, 1993",
        'header_image" : one_image_URL,
        'body_images"  : list_of_images,
        'body"         : "more raw text with <> anchors for images",
    }
"""
def get_sorted_blog_list():
    # @TODO call the database to get the collection
    # @TODO have a way for that collection to be updated with:
    #   1) All the blogs by featured authors (AKA Jared Amalong)
    #   2) Any specific articles that have been chosen via URL 
    return []

"""
Function get_5_blogs 
When the bottom of page is reached, 
this function will return 5 more blogs to be put on the page_display_list

#returns 5 more blog to be added to the list of blogs to display
"""

