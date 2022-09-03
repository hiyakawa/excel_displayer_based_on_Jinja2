Excel Displayer Based on Flask
==============================

A Flask B/S application to upload and display Excel files on web pages.

Copyright(c) 12/16/2021 Muyuan Zhang 

## Overview

This script is to convert excel files into HTML tables using Python Flask.

/select is to request the user to upload a valid file with an extension of .xls or .xlsx and to redirect to /result.

/result is to display the excel content at the front-end. If an unvalid file is uploaded, it will redirect back to /select and require the user to choose another file.
