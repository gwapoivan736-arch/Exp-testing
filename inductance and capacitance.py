 if gmd_values and gmr_values:   
            avg_gmd = geometric_mean(list(gmd_values.values()))
            avg_gmr = geometric_mean(list(gmr_values.values()))


            #Constants
            induc_const = 2e-7  # H/m
            ε = 8.854e-12  # F/m            

            # Inductance per meter (H/m)
            L_total = induc_const * np.log(avg_gmd / avg_gmr)

             # Capacitance per meter (F/m)
            C_total = (2 * np.pi * ε) / np.log(avg_gmd / avg_gmr)
            