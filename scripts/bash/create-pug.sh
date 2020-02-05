#!/bin/bash

mkdir $1
cd $1
touch config.rb
touch index.pug
mkdir 3-js
mkdir 1-partials
mkdir 0-views
mkdir -p 2-stylesheets/parts
touch 3-js/placeholder
touch 0-views/placeholder
touch 1-partials/placeholder
touch 2-stylesheets/styles.sass
mkdir 4-img
touch 4-img/placeholder

cat > config.rb <<EOF
require "compass/import-once/activate"

http_path = "/"
css_dir = "2-stylesheets"
sass_dir = "2-stylesheets"
javascripts_dir = "3-js"
images_dir = "4-img"
EOF

cat > index.pug <<EOF
doctype html
html
    head
        title $1
        meta(charset="utf-8")
        meta(name="viewport", content="widht=device-width, initial-scale=1")
        meta(name="theme-color", content="tomato")
        meta(http-equiv="X-UA-Compatible", content="IE=edge")
        link(rel="stylesheet", href="2-stylesheets/styles.css", type="text/css")
    body
        div.container
            section.main
                h1 $1
EOF

cat > 2-stylesheets/styles.sass <<EOF
*
    box-sizing: border-box
    
html, body
    background: tomato
    color: #fff
    font-family: Arial, "sans-serif"
    font-size: 100%
    margin: 0
    padding: 0
EOF
