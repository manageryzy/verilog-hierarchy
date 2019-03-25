def print_module(module):
    instance_str = ''
    for inst in module['instances'].values():
        instance_str += """
        <li><a href="#module-{}">{}</a> {} {} {}</li>
        """.format(
            inst['module'],
            inst['module'],
            inst['param'],
            inst['name'],
            inst['array']
        )

    res = '''
    <li>
        <h2><a name="{}">{}</a></h2>
        <h3>param</h3>
        <pre>{}</pre>
        <h3>signals</h3>
        <pre>{}</pre>
        <h3>instances</h3>
        <ul>
        {}
        </ul>
        <button onclick="$('#code-{}').show()">show code</button>
        <div id="code-{}" style=" display: none;">
        <pre class="prettyprint linenums"><code>{}</code></pre>
        </div>
    </li>
    '''.format(
        'module-' + module['name'],
        module['name'],
        module['param'],
        module['signals'],
        instance_str,
        module['name'],
        module['name'],
        module['raw']
    )
    return res


def print_modules(modules):
    modules_data = ""
    for module in modules.values():
        modules_data += print_module(module)
    return """
    <h1><a name="modules">modules</a></h1>
    <ul>
    {}
    </ul>
    """.format(
        modules_data
    )


def print_hierarchy(modules, name, depth=0):
    if depth > 10:
        return ""
    try:
        module = modules[name]
    except KeyError:
        return ""
    instance_str = ''
    for inst in module['instances'].values():
        instance_str += """
        <li><a href="#module-{}">{}</a> {} </li>
        """.format(
            inst['module'],
            inst['module'],
            inst['name'] + ' : ' + print_hierarchy(modules, inst['name'], depth + 1)
        )
    return ("""
    <h1><a name="hierarchy">hierarchy</a></h1>
    """ if depth is 0 else '') + """
    <ul>{}</ul>
    """.format(
        instance_str
    )


def print_html(modules, top=None):
    res = """
<html>
<head>
    <script src="https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"></script>
    <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js"></script>
</head>
<body>
{}
</body>
</html>
    """.format(
        print_modules(modules) + print_hierarchy(modules, str(top)) if top else
        print_modules(modules)
    )
    return res
