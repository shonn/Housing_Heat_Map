from django.contrib.gis.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

# 10-24-13 Alex Wu
# 	- Commented out all models except Zipcodeshapes and HouseData because those are the
#	models we'll actually use.
#   - import models from django.contrib.gis.db no enable GIS functionality
#   - Zipcodeshapes.geom is now a proper 
'''
class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True) # This field type is a guess.
    f_table_schema = models.TextField(blank=True) # This field type is a guess.
    f_table_name = models.TextField(blank=True) # This field type is a guess.
    f_geography_column = models.TextField(blank=True) # This field type is a guess.
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.TextField(blank=True)
    class Meta:
        db_table = u'geography_columns'

class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256, blank=True)
    f_table_schema = models.CharField(max_length=256, blank=True)
    f_table_name = models.CharField(max_length=256, blank=True)
    f_geometry_column = models.CharField(max_length=256, blank=True)
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'geometry_columns'

class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(null=True, blank=True)
    srtext = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)
    class Meta:
        db_table = u'spatial_ref_sys'

class RasterColumns(models.Model):
    r_table_catalog = models.TextField(blank=True) # This field type is a guess.
    r_table_schema = models.TextField(blank=True) # This field type is a guess.
    r_table_name = models.TextField(blank=True) # This field type is a guess.
    r_raster_column = models.TextField(blank=True) # This field type is a guess.
    srid = models.IntegerField(null=True, blank=True)
    scale_x = models.FloatField(null=True, blank=True)
    scale_y = models.FloatField(null=True, blank=True)
    blocksize_x = models.IntegerField(null=True, blank=True)
    blocksize_y = models.IntegerField(null=True, blank=True)
    same_alignment = models.NullBooleanField(null=True, blank=True)
    regular_blocking = models.NullBooleanField(null=True, blank=True)
    num_bands = models.IntegerField(null=True, blank=True)
    pixel_types = models.TextField(blank=True) # This field type is a guess.
    nodata_values = models.TextField(blank=True) # This field type is a guess.
    out_db = models.TextField(blank=True) # This field type is a guess.
    extent = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'raster_columns'

class RasterOverviews(models.Model):
    o_table_catalog = models.TextField(blank=True) # This field type is a guess.
    o_table_schema = models.TextField(blank=True) # This field type is a guess.
    o_table_name = models.TextField(blank=True) # This field type is a guess.
    o_raster_column = models.TextField(blank=True) # This field type is a guess.
    r_table_catalog = models.TextField(blank=True) # This field type is a guess.
    r_table_schema = models.TextField(blank=True) # This field type is a guess.
    r_table_name = models.TextField(blank=True) # This field type is a guess.
    r_raster_column = models.TextField(blank=True) # This field type is a guess.
    overview_factor = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'raster_overviews'

class GeocodeSettings(models.Model):
    name = models.TextField(primary_key=True)
    setting = models.TextField(blank=True)
    unit = models.TextField(blank=True)
    category = models.TextField(blank=True)
    short_desc = models.TextField(blank=True)
    class Meta:
        db_table = u'geocode_settings'

class DirectionLookup(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    abbrev = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'direction_lookup'

class SecondaryUnitLookup(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    abbrev = models.CharField(max_length=5, blank=True)
    class Meta:
        db_table = u'secondary_unit_lookup'

class StateLookup(models.Model):
    st_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, unique=True, blank=True)
    abbrev = models.CharField(max_length=3, unique=True, blank=True)
    statefp = models.CharField(max_length=2, unique=True, blank=True)
    class Meta:
        db_table = u'state_lookup'

class StreetTypeLookup(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    abbrev = models.CharField(max_length=50, blank=True)
    is_hw = models.BooleanField()
    class Meta:
        db_table = u'street_type_lookup'

class PlaceLookup(models.Model):
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True)
    pl_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'place_lookup'

class CountyLookup(models.Model):
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True)
    co_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'county_lookup'

class CountysubLookup(models.Model):
    st_code = models.IntegerField()
    state = models.CharField(max_length=2, blank=True)
    co_code = models.IntegerField()
    county = models.CharField(max_length=90, blank=True)
    cs_code = models.IntegerField()
    name = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'countysub_lookup'

class ZipLookupAll(models.Model):
    zip = models.IntegerField(null=True, blank=True)
    st_code = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=2, blank=True)
    co_code = models.IntegerField(null=True, blank=True)
    county = models.CharField(max_length=90, blank=True)
    cs_code = models.IntegerField(null=True, blank=True)
    cousub = models.CharField(max_length=90, blank=True)
    pl_code = models.IntegerField(null=True, blank=True)
    place = models.CharField(max_length=90, blank=True)
    cnt = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'zip_lookup_all'

class ZipLookupBase(models.Model):
    zip = models.CharField(max_length=5, primary_key=True)
    state = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=90, blank=True)
    city = models.CharField(max_length=90, blank=True)
    statefp = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'zip_lookup_base'

class ZipLookup(models.Model):
    zip = models.IntegerField(primary_key=True)
    st_code = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=2, blank=True)
    co_code = models.IntegerField(null=True, blank=True)
    county = models.CharField(max_length=90, blank=True)
    cs_code = models.IntegerField(null=True, blank=True)
    cousub = models.CharField(max_length=90, blank=True)
    pl_code = models.IntegerField(null=True, blank=True)
    place = models.CharField(max_length=90, blank=True)
    cnt = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'zip_lookup'

class County(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    countyns = models.CharField(max_length=8, blank=True)
    cntyidfp = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    namelsad = models.CharField(max_length=100, blank=True)
    lsad = models.CharField(max_length=2, blank=True)
    classfp = models.CharField(max_length=2, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    csafp = models.CharField(max_length=3, blank=True)
    cbsafp = models.CharField(max_length=5, blank=True)
    metdivfp = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.BigIntegerField(null=True, blank=True)
    awater = models.FloatField(null=True, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'county'

class State(models.Model):
    gid = models.IntegerField(unique=True)
    region = models.CharField(max_length=2, blank=True)
    division = models.CharField(max_length=2, blank=True)
    statefp = models.CharField(max_length=2, primary_key=True)
    statens = models.CharField(max_length=8, blank=True)
    stusps = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100, blank=True)
    lsad = models.CharField(max_length=2, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.BigIntegerField(null=True, blank=True)
    awater = models.BigIntegerField(null=True, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'state'

class Place(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True)
    placefp = models.CharField(max_length=5, blank=True)
    placens = models.CharField(max_length=8, blank=True)
    plcidfp = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    namelsad = models.CharField(max_length=100, blank=True)
    lsad = models.CharField(max_length=2, blank=True)
    classfp = models.CharField(max_length=2, blank=True)
    cpi = models.CharField(max_length=1, blank=True)
    pcicbsa = models.CharField(max_length=1, blank=True)
    pcinecta = models.CharField(max_length=1, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.BigIntegerField(null=True, blank=True)
    awater = models.BigIntegerField(null=True, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'place'

class ZipState(models.Model):
    zip = models.CharField(max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'zip_state'

class ZipStateLoc(models.Model):
    zip = models.CharField(max_length=5)
    stusps = models.CharField(max_length=2)
    statefp = models.CharField(max_length=2, blank=True)
    place = models.CharField(max_length=100)
    class Meta:
        db_table = u'zip_state_loc'

class Cousub(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    cousubfp = models.CharField(max_length=5, blank=True)
    cousubns = models.CharField(max_length=8, blank=True)
    cosbidfp = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    namelsad = models.CharField(max_length=100, blank=True)
    lsad = models.CharField(max_length=2, blank=True)
    classfp = models.CharField(max_length=2, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    cnectafp = models.CharField(max_length=3, blank=True)
    nectafp = models.CharField(max_length=5, blank=True)
    nctadvfp = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.DecimalField(null=True, max_digits=14, decimal_places=0, blank=True)
    awater = models.DecimalField(null=True, max_digits=14, decimal_places=0, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'cousub'

class Edges(models.Model):
    gid = models.IntegerField(primary_key=True)
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tlid = models.BigIntegerField(null=True, blank=True)
    tfidl = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    tfidr = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    smid = models.CharField(max_length=22, blank=True)
    lfromadd = models.CharField(max_length=12, blank=True)
    ltoadd = models.CharField(max_length=12, blank=True)
    rfromadd = models.CharField(max_length=12, blank=True)
    rtoadd = models.CharField(max_length=12, blank=True)
    zipl = models.CharField(max_length=5, blank=True)
    zipr = models.CharField(max_length=5, blank=True)
    featcat = models.CharField(max_length=1, blank=True)
    hydroflg = models.CharField(max_length=1, blank=True)
    railflg = models.CharField(max_length=1, blank=True)
    roadflg = models.CharField(max_length=1, blank=True)
    olfflg = models.CharField(max_length=1, blank=True)
    passflg = models.CharField(max_length=1, blank=True)
    divroad = models.CharField(max_length=1, blank=True)
    exttyp = models.CharField(max_length=1, blank=True)
    ttyp = models.CharField(max_length=1, blank=True)
    deckedroad = models.CharField(max_length=1, blank=True)
    artpath = models.CharField(max_length=1, blank=True)
    persist = models.CharField(max_length=1, blank=True)
    gcseflg = models.CharField(max_length=1, blank=True)
    offsetl = models.CharField(max_length=1, blank=True)
    offsetr = models.CharField(max_length=1, blank=True)
    tnidf = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    tnidt = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'edges'

class Addrfeat(models.Model):
    gid = models.IntegerField(primary_key=True)
    tlid = models.BigIntegerField(null=True, blank=True)
    statefp = models.CharField(max_length=2)
    aridl = models.CharField(max_length=22, blank=True)
    aridr = models.CharField(max_length=22, blank=True)
    linearid = models.CharField(max_length=22, blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    lfromhn = models.CharField(max_length=12, blank=True)
    ltohn = models.CharField(max_length=12, blank=True)
    rfromhn = models.CharField(max_length=12, blank=True)
    rtohn = models.CharField(max_length=12, blank=True)
    zipl = models.CharField(max_length=5, blank=True)
    zipr = models.CharField(max_length=5, blank=True)
    edge_mtfcc = models.CharField(max_length=5, blank=True)
    parityl = models.CharField(max_length=1, blank=True)
    parityr = models.CharField(max_length=1, blank=True)
    plus4l = models.CharField(max_length=4, blank=True)
    plus4r = models.CharField(max_length=4, blank=True)
    lfromtyp = models.CharField(max_length=1, blank=True)
    ltotyp = models.CharField(max_length=1, blank=True)
    rfromtyp = models.CharField(max_length=1, blank=True)
    rtotyp = models.CharField(max_length=1, blank=True)
    offsetl = models.CharField(max_length=1, blank=True)
    offsetr = models.CharField(max_length=1, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'addrfeat'

class Faces(models.Model):
    gid = models.IntegerField(primary_key=True)
    tfid = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    statefp00 = models.CharField(max_length=2, blank=True)
    countyfp00 = models.CharField(max_length=3, blank=True)
    tractce00 = models.CharField(max_length=6, blank=True)
    blkgrpce00 = models.CharField(max_length=1, blank=True)
    blockce00 = models.CharField(max_length=4, blank=True)
    cousubfp00 = models.CharField(max_length=5, blank=True)
    submcdfp00 = models.CharField(max_length=5, blank=True)
    conctyfp00 = models.CharField(max_length=5, blank=True)
    placefp00 = models.CharField(max_length=5, blank=True)
    aiannhfp00 = models.CharField(max_length=5, blank=True)
    aiannhce00 = models.CharField(max_length=4, blank=True)
    comptyp00 = models.CharField(max_length=1, blank=True)
    trsubfp00 = models.CharField(max_length=5, blank=True)
    trsubce00 = models.CharField(max_length=3, blank=True)
    anrcfp00 = models.CharField(max_length=5, blank=True)
    elsdlea00 = models.CharField(max_length=5, blank=True)
    scsdlea00 = models.CharField(max_length=5, blank=True)
    unsdlea00 = models.CharField(max_length=5, blank=True)
    uace00 = models.CharField(max_length=5, blank=True)
    cd108fp = models.CharField(max_length=2, blank=True)
    sldust00 = models.CharField(max_length=3, blank=True)
    sldlst00 = models.CharField(max_length=3, blank=True)
    vtdst00 = models.CharField(max_length=6, blank=True)
    zcta5ce00 = models.CharField(max_length=5, blank=True)
    tazce00 = models.CharField(max_length=6, blank=True)
    ugace00 = models.CharField(max_length=5, blank=True)
    puma5ce00 = models.CharField(max_length=5, blank=True)
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tractce = models.CharField(max_length=6, blank=True)
    blkgrpce = models.CharField(max_length=1, blank=True)
    blockce = models.CharField(max_length=4, blank=True)
    cousubfp = models.CharField(max_length=5, blank=True)
    submcdfp = models.CharField(max_length=5, blank=True)
    conctyfp = models.CharField(max_length=5, blank=True)
    placefp = models.CharField(max_length=5, blank=True)
    aiannhfp = models.CharField(max_length=5, blank=True)
    aiannhce = models.CharField(max_length=4, blank=True)
    comptyp = models.CharField(max_length=1, blank=True)
    trsubfp = models.CharField(max_length=5, blank=True)
    trsubce = models.CharField(max_length=3, blank=True)
    anrcfp = models.CharField(max_length=5, blank=True)
    ttractce = models.CharField(max_length=6, blank=True)
    tblkgpce = models.CharField(max_length=1, blank=True)
    elsdlea = models.CharField(max_length=5, blank=True)
    scsdlea = models.CharField(max_length=5, blank=True)
    unsdlea = models.CharField(max_length=5, blank=True)
    uace = models.CharField(max_length=5, blank=True)
    cd111fp = models.CharField(max_length=2, blank=True)
    sldust = models.CharField(max_length=3, blank=True)
    sldlst = models.CharField(max_length=3, blank=True)
    vtdst = models.CharField(max_length=6, blank=True)
    zcta5ce = models.CharField(max_length=5, blank=True)
    tazce = models.CharField(max_length=6, blank=True)
    ugace = models.CharField(max_length=5, blank=True)
    puma5ce = models.CharField(max_length=5, blank=True)
    csafp = models.CharField(max_length=3, blank=True)
    cbsafp = models.CharField(max_length=5, blank=True)
    metdivfp = models.CharField(max_length=5, blank=True)
    cnectafp = models.CharField(max_length=3, blank=True)
    nectafp = models.CharField(max_length=5, blank=True)
    nctadvfp = models.CharField(max_length=5, blank=True)
    lwflag = models.CharField(max_length=1, blank=True)
    offset = models.CharField(max_length=1, blank=True)
    atotal = models.FloatField(null=True, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'faces'

class Featnames(models.Model):
    gid = models.IntegerField(primary_key=True)
    tlid = models.BigIntegerField(null=True, blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    predirabrv = models.CharField(max_length=15, blank=True)
    pretypabrv = models.CharField(max_length=50, blank=True)
    prequalabr = models.CharField(max_length=15, blank=True)
    sufdirabrv = models.CharField(max_length=15, blank=True)
    suftypabrv = models.CharField(max_length=50, blank=True)
    sufqualabr = models.CharField(max_length=15, blank=True)
    predir = models.CharField(max_length=2, blank=True)
    pretyp = models.CharField(max_length=3, blank=True)
    prequal = models.CharField(max_length=2, blank=True)
    sufdir = models.CharField(max_length=2, blank=True)
    suftyp = models.CharField(max_length=3, blank=True)
    sufqual = models.CharField(max_length=2, blank=True)
    linearid = models.CharField(max_length=22, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    paflag = models.CharField(max_length=1, blank=True)
    statefp = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'featnames'

class Addr(models.Model):
    gid = models.IntegerField(primary_key=True)
    tlid = models.BigIntegerField(null=True, blank=True)
    fromhn = models.CharField(max_length=12, blank=True)
    tohn = models.CharField(max_length=12, blank=True)
    side = models.CharField(max_length=1, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    plus4 = models.CharField(max_length=4, blank=True)
    fromtyp = models.CharField(max_length=1, blank=True)
    totyp = models.CharField(max_length=1, blank=True)
    fromarmid = models.IntegerField(null=True, blank=True)
    toarmid = models.IntegerField(null=True, blank=True)
    arid = models.CharField(max_length=22, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    statefp = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'addr'

class Zcta5(models.Model):
    gid = models.IntegerField(unique=True)
    statefp = models.CharField(max_length=2)
    zcta5ce = models.CharField(max_length=5)
    classfp = models.CharField(max_length=2, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.FloatField(null=True, blank=True)
    awater = models.FloatField(null=True, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    partflg = models.CharField(max_length=1, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'zcta5'

class LoaderPlatform(models.Model):
    os = models.CharField(max_length=50, primary_key=True)
    declare_sect = models.TextField(blank=True)
    pgbin = models.TextField(blank=True)
    wget = models.TextField(blank=True)
    unzip_command = models.TextField(blank=True)
    psql = models.TextField(blank=True)
    path_sep = models.TextField(blank=True)
    loader = models.TextField(blank=True)
    environ_set_command = models.TextField(blank=True)
    county_process_command = models.TextField(blank=True)
    class Meta:
        db_table = u'loader_platform'

class LoaderVariables(models.Model):
    tiger_year = models.CharField(max_length=4, primary_key=True)
    website_root = models.TextField(blank=True)
    staging_fold = models.TextField(blank=True)
    data_schema = models.TextField(blank=True)
    staging_schema = models.TextField(blank=True)
    class Meta:
        db_table = u'loader_variables'

class LoaderLookuptables(models.Model):
    process_order = models.IntegerField()
    lookup_name = models.TextField(primary_key=True)
    table_name = models.TextField(blank=True)
    single_mode = models.BooleanField()
    load = models.BooleanField()
    level_county = models.BooleanField()
    level_state = models.BooleanField()
    level_nation = models.BooleanField()
    post_load_process = models.TextField(blank=True)
    single_geom_mode = models.NullBooleanField(null=True, blank=True)
    insert_mode = models.CharField(max_length=1)
    pre_load_process = models.TextField(blank=True)
    columns_exclude = models.TextField(blank=True) # This field type is a guess.
    website_root_override = models.TextField(blank=True)
    class Meta:
        db_table = u'loader_lookuptables'

class Tract(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tractce = models.CharField(max_length=6, blank=True)
    tract_id = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=7, blank=True)
    namelsad = models.CharField(max_length=20, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.FloatField(null=True, blank=True)
    awater = models.FloatField(null=True, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'tract'

class Tabblock(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tractce = models.CharField(max_length=6, blank=True)
    blockce = models.CharField(max_length=4, blank=True)
    tabblock_id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    ur = models.CharField(max_length=1, blank=True)
    uace = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.FloatField(null=True, blank=True)
    awater = models.FloatField(null=True, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'tabblock'
'''
class Zipcodeshapes(models.Model):
	gid = models.IntegerField(primary_key=True)
	zcta5ce10 = models.CharField(max_length=5, blank=True)
	geoid10 = models.CharField(max_length=5, blank=True)
	classfp10 = models.CharField(max_length=2, blank=True)
	mtfcc10 = models.CharField(max_length=5, blank=True)
	funcstat10 = models.CharField(max_length=1, blank=True)
	aland10 = models.FloatField(null=True, blank=True)
	awater10 = models.FloatField(null=True, blank=True)
	intptlat10 = models.CharField(max_length=11, blank=True)
	intptlon10 = models.CharField(max_length=12, blank=True)
	geom = models.MultiPolygonField(srid=4269, blank=True)
	objects = models.GeoManager()
	
	def __unicode__(self):
		return self.zcta5ce10
	class Meta:
		db_table = u'zipcodeshapes'
'''
class Bg(models.Model):
    gid = models.IntegerField()
    statefp = models.CharField(max_length=2, blank=True)
    countyfp = models.CharField(max_length=3, blank=True)
    tractce = models.CharField(max_length=6, blank=True)
    blkgrpce = models.CharField(max_length=1, blank=True)
    bg_id = models.CharField(max_length=12, primary_key=True)
    namelsad = models.CharField(max_length=13, blank=True)
    mtfcc = models.CharField(max_length=5, blank=True)
    funcstat = models.CharField(max_length=1, blank=True)
    aland = models.FloatField(null=True, blank=True)
    awater = models.FloatField(null=True, blank=True)
    intptlat = models.CharField(max_length=11, blank=True)
    intptlon = models.CharField(max_length=12, blank=True)
    the_geom = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'bg'

class PagcGaz(models.Model):
    id = models.IntegerField(primary_key=True)
    seq = models.IntegerField(null=True, blank=True)
    word = models.TextField(blank=True)
    stdword = models.TextField(blank=True)
    token = models.IntegerField(null=True, blank=True)
    is_custom = models.BooleanField()
    class Meta:
        db_table = u'pagc_gaz'

class PagcLex(models.Model):
    id = models.IntegerField(primary_key=True)
    seq = models.IntegerField(null=True, blank=True)
    word = models.TextField(blank=True)
    stdword = models.TextField(blank=True)
    token = models.IntegerField(null=True, blank=True)
    is_custom = models.BooleanField()
    class Meta:
        db_table = u'pagc_lex'

class PagcRules(models.Model):
    id = models.IntegerField(primary_key=True)
    rule = models.TextField(blank=True)
    is_custom = models.NullBooleanField(null=True, blank=True)
    class Meta:
        db_table = u'pagc_rules'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = u'auth_group'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'
'''
class HouseData(models.Model):
    house_zip = models.CharField(max_length=5, primary_key=True)
    house_date = models.CharField(max_length=10)
    house_price = models.FloatField()
    class Meta:
        unique_together = (("house_zip", "house_date"),)
        db_table = u'house_data'
'''
class Zipcode(models.Model):
	gid = models.IntegerField(primary_key=True)
	zcta5ce10 = models.CharField(max_length=5, blank=True)
	geoid10 = models.CharField(max_length=5, blank=True)
	classfp10 = models.CharField(max_length=2, blank=True)
	mtfcc10 = models.CharField(max_length=5, blank=True)
	funcstat10 = models.CharField(max_length=1, blank=True)
	aland10 = models.FloatField(null=True, blank=True)
	awater10 = models.FloatField(null=True, blank=True)
	intptlat10 = models.CharField(max_length=11, blank=True)
	intptlon10 = models.CharField(max_length=12, blank=True)
	geom = models.MultiPolygonField(srid=4269, blank=True)
	objects = models.GeoManager()
	
	def __unicode__(self):
		return self.zcta5ce10
		
class HousingPriceByZip(models.Model):
	zipcode = models.ForeignKey(Zipcode)
	date = models.DateField()
	price = models.Float()
	'''
