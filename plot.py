Tcmb_uK = 2.7255e6 
ell = output_camb_format[0]
Cl_TT =  output_class_format[1] # == output_camb_format[1]/Tcmb_uK**2
Cl_TT_uK =  output_camb_format[1] # == output_class_format[1]*Tcmb_uK**2
Cl_TG = output_camb_format[10] # == output_class_format[10]
Cl_TG_uK = output_camb_format[10]*Tcmb_uK # == output_camb_format[10]*Tcmb_uK
Cl_GG = output_camb_format[5] # == output_class_format[5]
sigma_CV = np.sqrt(4*np.pi/(2*ell+1)*(Cl_TG**2+Cl_GG*Cl_TT))
sigma_CV_uK = np.sqrt(4*np.pi/(2*ell+1)*(Cl_TG_uK**2+Cl_GG*Cl_TT_uK))

plt.errorbar(ell, Cl_TG, yerr=sigma_CV)
plt.xlim(0, 500)
plt.show()
plt.errorbar(ell, Cl_TG_uK, yerr=sigma_CV_uK)
plt.xlim(0, 500)
plt.show()


plt.plot(ell, Cl_TT)
plt.plot(ell, Cl_TG)
plt.loglog(ell, Cl_GG)
plt.show()

plt.plot(ell, Cl_TT*Cl_GG, label=r'$C_\ell^{TT}\cdot C_\ell^{GG}$')
plt.loglog(ell, Cl_TG**2, label=r'$(C_\ell^{TG})^2$')
plt.legend()
plt.xlim(0, 500)
plt.xlabel(r"$\ell$")
plt.ylabel(r"$C_\ell^2$")
plt.tight_layout()
plt.show()
