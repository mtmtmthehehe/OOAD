#!/usr/bin/env bash
# Render toàn bộ file .puml trong docs/ sang .png
cd "$(dirname "$0")/.."
find docs -name '*.puml' -exec java -jar scripts/plantuml.jar -tpng {} +
