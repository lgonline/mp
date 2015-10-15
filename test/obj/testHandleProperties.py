__author__ = 'Administrator'

from obj.handleProperties import Japanese

if __name__ == "__main__":
    tzry = Japanese()
    #access the public propery in this class
    print("tzry's nationnality is : ",tzry.nationality)
    #access the private property in this class
    print("tzry's age is : ",tzry._Japanese__age)

    print("--------print for some inner properties--------------")
    #print("tzry.__bases__ is : ",tzry.__bases__)
    print("tzry.__dict__ is : ",tzry.__dict__)
    print("tzry.__module__ is : ",tzry.__module__)
    print("tzry.__doc__ is : ",tzry.__doc__)
    #print("tzry.__name__ is : ",tzry.__name__)