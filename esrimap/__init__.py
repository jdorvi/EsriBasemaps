# -*- coding: utf-8 -*-
"""
/***************************************************************************
 esrimap
                                 A QGIS plugin
 Loads basemaps from the Esri restful API
                             -------------------
        begin                : 2016-08-03
        copyright            : (C) 2016 by J. Dorvinen
        email                : jdorvi@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load esrimap class from file esrimap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .esri_basemap import esrimap
    return esrimap(iface)
