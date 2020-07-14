import camelcase

# pip needs permission to install packages so always remember to use sudo.

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
