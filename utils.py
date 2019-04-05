##
## Truncate characters of a string after _len'nth char, if necessary... If _len is less than 0, don't truncate anything... Note: If you attach a suffix, and you enable absolute max length then the suffix length is subtracted from max length... Note: If the suffix length is longer than the output then no suffix is used...
##
## Usage: Where _text = 'Testing', _width = 4
##      _data = String.Truncate( _text, _width )                        == Test
##      _data = String.Truncate( _text, _width, '..', True )            == Te..
##
## Equivalent Alternates: Where _text = 'Testing', _width = 4
##      _data = String.SubStr( _text, 0, _width )                       == Test
##      _data = _text[  : _width ]                                      == Test
##      _data = ( _text )[  : _width ]                                  == Test
##
def Truncate( _text, _max_len = -1, _suffix = False, _absolute_max_len = True ):
    ## Length of the string we are considering for truncation
    _len            = len( _text )

    ## Whether or not we have to truncate
    _truncate       = ( False, True )[ _len > _max_len ]

    ## Note: If we don't need to truncate, there's no point in proceeding...
    if ( not _truncate ):
        return _text

    ## The suffix in string form
    _suffix_str     = ( '',  str( _suffix ) )[ _truncate and _suffix != False ]

    ## The suffix length
    _len_suffix     = len( _suffix_str )

    ## Whether or not we add the suffix
    _add_suffix     = ( False, True )[ _truncate and _suffix != False and _max_len > _len_suffix ]

    ## Suffix Offset
    _suffix_offset = _max_len - _len_suffix
    _suffix_offset  = ( _max_len, _suffix_offset )[ _add_suffix and _absolute_max_len != False and _suffix_offset > 0 ]

    ## The truncate point.... If not necessary, then length of string.. If necessary then the max length with or without subtracting the suffix length... Note: It may be easier ( less logic cost ) to simply add the suffix to the calculated point, then truncate - if point is negative then the suffix will be destroyed anyway.
    ## If we don't need to truncate, then the length is the length of the string.. If we do need to truncate, then the length depends on whether we add the suffix and offset the length of the suffix or not...
    _len_truncate   = ( _len, _max_len )[ _truncate ]
    _len_truncate   = ( _len_truncate, _max_len )[ _len_truncate <= _max_len ]

    ## If we add the suffix, add it... Suffix won't be added if the suffix is the same length as the text being output...
    if ( _add_suffix ):
        _text = _text[ 0 : _suffix_offset ] + _suffix_str + _text[ _suffix_offset: ]

    ## Return the text after truncating...
    return _text[ : _len_truncate ]
