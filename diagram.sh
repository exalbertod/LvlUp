#!/bin/bash

echo "📄 Generando schema.er desde SQLite..."
pipenv run eralchemy -i sqlite:////tmp/test.db -o schema.er

echo "🖼️ Generando imagen diagram.png..."
pipenv run eralchemy -i schema.er -o diagram.png

echo "✅ Diagrama generado como diagram.png"
