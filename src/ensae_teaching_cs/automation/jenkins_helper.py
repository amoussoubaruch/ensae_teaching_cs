"""
@file
@brief Set up a jenkins server with all the necessary job
"""
import re
from pyquickhelper.loghelper import noLOG
from pyquickhelper.jenkinshelper import setup_jenkins_server_yml


def engines_default():
    """
    returns a dictionary with default values for Jenkins server

    @return     dictionary

    .. warning::

        Virtual environment with conda must be created on the same disk
        as the original interpreter. The other scenario is not supported.
    """
    res = dict(anaconda2="d:\\Anaconda",
               anaconda3="d:\\Anaconda3",
               py35="c:\\Python35_x64",
               py34="c:\\Python34_x64",
               py27="c:\\Python27",
               default="c:\\Python35_x64",
               winpython="c:\\APythonENSAE\\python",
               Python35pyq="D:\\jenkins\\venv\\py35\\pyq\\Scripts")
    res["Python27"] = res["py27"]
    res["Python34"] = res["py34"]
    res["Python35"] = res["py35"]
    res["Anaconda2"] = res["anaconda2"]
    res["Anaconda3"] = res["anaconda3"]
    res["WinPython35"] = res["winpython"]
    return res


def default_jenkins_jobs(filter=None, neg_filter=None, root=None):
    """
    default list of Jenkins jobs

    @param      filter          keep a subset of jobs (regular expression)
    @param      neg_filter      remove a subset of jobs (regular expression)
    @param      root            where to find yml project
    @return                     list

    It produces a subset of the following list of jobs:

    .. runpython::

        import textwrap
        from ensae_teaching_cs.automation.jenkins_helper import default_jenkins_jobs
        modules = default_jenkins_jobs()
        text = str(modules)
        print(textwrap.wrap(text))

    """
    yml = []
    pattern = "https://raw.githubusercontent.com/sdpython/%s/master/.local.jenkins.win.yml"
    modules = ["pyquickhelper", "python3_module_template", "pymmails", "pymyinstall",
               "pyensae", "pyrsslocal", "pysqllike", "ensae_projects",
               "ensae_teaching_cs", "code_beatrix", "actuariat_python", "mlstatpy", "jupytalk"]
    for c in modules:
        yml.append(pattern % c)

    if filter is not None or neg_filter is not None:
        reg = re.compile(filter if filter else ".*")
        neg_reg = re.compile(neg_filter if neg_filter else "^$")
        res = default_jenkins_jobs()
        new_res = []
        for row in res:
            if isinstance(row, str):
                if reg.search(row) and not neg_reg.search(row):
                    new_res.append(row)
            elif isinstance(row, tuple):
                if reg.search(row[0]) and not neg_reg.search(row[0]):
                    new_res.append(row)
            elif isinstance(row, list):
                # list
                sub = []
                for item in row:
                    if isinstance(item, str):
                        if reg.search(item) and not neg_reg.search(item):
                            sub.append(item)
                    elif isinstance(item, tuple):
                        if reg.search(item[0]) and not neg_reg.search(item[0]):
                            sub.append(item)
                    else:
                        raise TypeError("{0} - {1}".format(item, type(item)))
                if len(sub) > 0:
                    new_res.append(sub)
            else:
                raise TypeError("{0} - {1}".format(row, type(row)))
        return new_res
    else:
        res = []
        res.extend(('yml', c, 'H H(0-1) * * %d' % (i % 7))
                   for i, c in enumerate(yml))
        res += [("standalone [conda_update] [anaconda3]", "H H(0-1) * * 0"),
                "standalone [conda_update] [anaconda2] [27]",
                "standalone [local_pypi]",
                # update
                ("pymyinstall [update_modules]", "H H(0-1) * * 5"),
                "pymyinstall [update_modules] [winpython]",
                "pymyinstall [update_modules] [py34]",
                "pymyinstall [update_modules] [py27]",
                "pymyinstall [update_modules] [anaconda2]",
                "pymyinstall [update_modules] [anaconda3]",
                ]
        return res


def setup_jenkins_server(js, github="sdpython", modules=default_jenkins_jobs(),
                         overwrite=False, location=None, prefix="",
                         delete_first=False, fLOG=noLOG):
    """
    Set up many jobs on Jenkins

    @param      js                      (JenkinsExt) jenkins server (specially if you need credentials)
    @param      github                  github account if it does not start with *http://*,
                                        the link to git repository of the project otherwise
    @param      modules                 modules for which to generate the Jenkins job (see @see fn default_jenkins_jobs)
    @param      get_jenkins_script      see `get_jenkins_script <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/jenkinshelper/jenkins_server.html?highlight=get_jenkins_script#pyquickhelper.jenkinshelper.jenkins_server.JenkinsExt.get_jenkins_script>`_
                                        (default value if this parameter is None)
    @param      overwrite               do not create the job if it already exists
    @param      location                None for default or a local folder
    @param      prefix                  add a prefix to the name
    @param      delete_first            remove all jobs first
    @param      fLOG                    logging function
    @return                             list of created jobs

    *modules* is a list defined as follows:

    * each element can be a string or a tuple (string, schedule time) or a list
    * if it is a list, it contains a list of elements defined as previously
    * the job at position i is not scheduled, it will start after the last
      job at position i-1 whether or not it fails
    """
    r = setup_jenkins_server_yml(js, github=github, modules=modules, get_jenkins_script=None,
                                 overwrite=overwrite, location=location, prefix=prefix,
                                 delete_first=delete_first)
    return r
