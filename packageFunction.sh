mkdir -p build
zip -r build/pythonFunction.zip src/*
aws lambda update-function-code --function-name pythonFunction --zip-file fileb://build/pythonFunction.zip > /dev/null
aws lambda update-function-configuration --function-name pythonFunction --handler src/function.lambda_handler > /dev/null