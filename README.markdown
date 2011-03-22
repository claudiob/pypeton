
An application to bootstrap 

Frequently we need to create a Django project from scratch and push it on a production machine. 
**pypeton** helps reduce the number of manual steps to achieve this goal.


## Installation
    
    pip install -e git+git://github.com/ff0000/pypeton.git


## Usage

    pypeton [options] project_name
    
### Options

      --version          show program's version number and exit
      -h, --help         show this help message and exit
      -v, --virtualenv   initialise virtual envirnment
      -s, --subversion   create project in svn style with trunk/tags/branches
      -d DIR, --dir=DIR  base project directory
      -e ENV, --env=ENV  [bongo] or [django]
      
### Examples

Most basic project

    pypeton my_project
    
    
Build out an svn folder structure, insert a django project into trunk, and 
initialize a virtual environment all in one step.

    pypeton -s -v my_project  
    
Specify a directory other than the present working directory

    pypeton -d /path/to/folder  my_project
    
Create complete chaos ( a bongo project )

    pypeton -e bongo  my_project
    
    
## TODO: 

Add description of project customization:

* how to define requirements
* what's in which folder



## Installing requirements

The next step is to install the requirements for the project, with these commands:

    cd fooapp/trunk
    source activate
    cd project
    ./req

where `.req` is a provided shortcut for "pip install -r ../deploy/requirements.txt"

## Running the project in the browser

The project comes with an empty home-page which can be seen in a web browser by running:

    python manage.py syncdb --settings=settings.development
    ./ser development

and then opening [http://localhost:8000/](http://localhost:8000/) in a browser window. `./ser` is a shortcut provided for the command `python manage.py runserver 0.0.0.0:8000 --settings=settings.$1` used frequently to start the local server.

## Resetting the database and loading fixtures
 
The project also comes with an application named *initial_data*, a model with a fixture to create in the development environment an *admin* user with password *admin* and a site called http://example.com:8000. These data can be loaded by running:

    ./syn development

where `./syn` is a shortcut to:

* reset the database structure 
* synchronize it again with the latest models
* optionally reload the fixtures for the specified environment (in this case, users and sites for development)

At this point, Django admin can be accessed by running `./ser development` again, then logging into [http://example.com:8000/admin](http://example.com:8000/admin) with admin/admin (make sure to have "example.com" in the machine hosts file pointing to the localhost).

## Creating a new model and application

A new model (e.g., called *Picture*) can be created with the command:

    ./sta Picture

which extends the default "python manage.py startapp" command by delivering a coherent file structure and providing two basic views for index and show. To include this model in the application:

* add `'pictures',` to `INSTALLED_APPS` in settings/\_\_init\_\_.py, and
* add `(r'^pictures/', include('pictures.urls'))` to `urlpatterns` in urls.py.
* run `./syn development` to add the model to the database

At this point, all these new views become available:

* http://example.com:8000/admin/pictures/picture/add/ (to add a picture)
* http://example.com:8000/admin/pictures/picture/ (to admin the pictures)
* http://example.com:8000/pictures/ (to show the list of pictures)
* http://example.com:8000/pictures/1/ (to show one picture after its creation)

## Customizing the model

The newly created model can be edited at will. For instance, the Picture model can be inherited by [django-imagekit](https://github.com/jdriscoll/django-imagekit)'s ImageModel in order to have many image-related functions available. For this purpose:

<!-- requirements should also be split according to the environment! -->

* add the following lines to deploy/requirements.txt:

        pil                  # to use models.ImageField
        django-imagekit      # to deal with image size, thumbnails

* run the command `./req` to install the new requirements

* edit apps/pictures/models.py to begin as:

        from django.db import models
        from imagekit.models import ImageModel
        
        class Picture(ImageModel):
            name = models.CharField(max_length=255)
            image = models.ImageField(upload_to='uploads')
            num_views = models.PositiveIntegerField(editable=False, default=0)
            #
            class IKOptions:
                # This inner class is where we define the ImageKit options for the model
                spec_module   = 'pictures.specs'
                cache_dir     = 'cache'
                image_field   = 'image'
                save_count_as = 'num_views'
  
* add apps/pictures/specs.py as:

        from imagekit.specs import ImageSpec
        from imagekit import processors
        
        # first we define our thumbnail resize processor
        class ResizeThumb(processors.Resize):
            width =  20
            height = 20
            crop = True
        
        # now we can define our thumbnail spec
        class Thumbnail(ImageSpec):
            access_as = 'thumbnail_image'
            pre_cache = True
            processors = [ResizeThumb]
        
* change the loop in template/pictures/index.html as:

        {% for picture in pictures %}
            <li><a href={{ picture.get_absolute_url }}>
              {{ picture.id }}
              <img src="{{ picture.thumbnail_image.url}}" />
            </a></li>
        {% endfor %}

* add `<img src="{{picture.image.url}}" />` to the content in templates/pictures/show.html

At this point, run `./syn development` to adjust the database in order the include the Imagekit fields into the Picture table. Then the following views allow to:

* http://example.com:8000/admin/pictures/picture/add/ (add a picture with an attached image)
* http://example.com:8000/pictures/ (see the list of images with a thumbnail)
* http://example.com:8000/pictures/1/ (see the original image inserted)

## Creating fixtures

Whenever the `./syn` command is run, all the data in the database is deleted. The method not to lose data during a synchronization is using fixtures.

For instance, after adding a Picture through the admin interface, this can be stored in a fixture running:

    ./dum pictures development

where `./dum` is a shortcut for `python manage.py dumpdata` to output the data with the right indentation in the specified environment.

At this point, running `.syn development` again will reset the database and reload the images from the fixtures, without losing any data in the operation.

## Storing uploads on a CDN

For local development, storing uploads (such as images) in the same folder as the Django code is fine. But this is not the desired behavior on staging or production machines. Uploads can be easily stored in [Rackspace CDN](http://www.rackspace.com/cloud/) by using [django-cumulus](https://github.com/richleland/django-cumulus):

* log into Rackspace cloud and create a new container
* add the following line to deploy/requirements.txt:

        django-cumulus       # to store uploads on CDN

* run the command `./req` to install the new requirement
* add the following lines to settings/staging.py:

        INSTALLED_APPS = INSTALLED_APPS + (
            'cumulus',
        )

        DEFAULT_FILE_STORAGE     = 'cumulus.storage.CloudFilesStorage'
        CUMULUS_USERNAME         = '[Your Rackspace Cloud username]'
        CUMULUS_API_KEY          = '[Your Rackspace Cloud API key]'
        CUMULUS_CONTAINER        = '[Your Rackspace Cloud container]'
        CUMULUS_FILTER_LIST      = ['.DS_Store']
        CUMULUS_STATIC_CONTAINER = CUMULUS_CONTAINER
        CUMULUS_USE_SERVICENET   = False
        STATIC_URL               = ""

At this point, run `./syn staging` to set up a database for the staging server (which, for now, is on the same development machine). Since it's a staging server, an admin/admin user will not be created automatically, but prompted, in order to use a valid password. 

Then run `./ser staging` to run the server with the staging settings. All the pictures will then be uploaded to the CDN and not to any local folder.

It is also possible to batch upload all the pictures loaded so far in the development machine onto the CDN server that serves the staging environment by running:

    ./upl staging



