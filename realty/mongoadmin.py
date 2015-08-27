
# Import the MongoAdmin base class
from mongonaut.sites import MongoAdmin
# Import your custom models
from models import Advert, Advert_Users, Profile, ProfileAgency, Ticket, User
# Subclass MongoAdmin and add a customization
class AdvertAdmin(MongoAdmin):
	# Searches on the title field. Displayed in the DocumentListView.
	search_fields = ('username','id',)
	# provide following fields for view in the DocumentListView
	list_fields = ('status','owner','region','action_type','cat_tab','cat_type',)
	# Instantiate the PostAdmin subclass
	# Then attach PostAdmin to your m

Advert.mongoadmin = AdvertAdmin()

class AdvertUserAdmin(MongoAdmin):
	# Searches on the title field. Displayed in the DocumentListView.
	search_fields = ('username','id',)
	# provide following fields for view in the DocumentListView
	list_fields = ('status','owner','region','action_type','cat_tab','cat_type',)
	# Instantiate the PostAdmin subclass
	# Then attach PostAdmin to your m

Advert_Users.mongoadmin = AdvertUserAdmin()

class ProfileAdmin(MongoAdmin):
	search_fields = ('title','id',)
	list_fields = ('username','email',)

Profile.mongoadmin = ProfileAdmin()

class ProfileAgencyAdmin(MongoAdmin):
	search_fields = ('username','id',)
	list_fields = ('username','email','name_of_entity','head_name',)

ProfileAgency.mongoadmin = ProfileAgencyAdmin()

class TicketAdmin(MongoAdmin):
	search_fields = ('name','id',)
	list_fields = ('name','email','phone','text',)

Ticket.mongoadmin = TicketAdmin()

class UserAdmin(MongoAdmin):
	search_fields = ('username','email','id',)
	list_fields = ('name','email','phone','is_active',)

User.mongoadmin = UserAdmin()