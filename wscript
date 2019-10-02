#!/usr/bin/env python
# encoding: utf-8

from waflib import Build, ConfigSet, Configure, Context, Utils

def options( opt ):
        opt.load( 'compiler_c compiler_cxx' )

def configure( cnfg ):
        cnfg.load( 'compiler_c compiler_cxx' )
        cnfg.check( features='cxx cxxprogram', cflags=['-Wall'] )

# figure out how to make this autodetect src files in project structure
def build( bld ):
        bld( features='c cshlib', source='sources' target='target_name' )
        bld( features='c cxx cxxprogram', source='sources', target='target_name' )
