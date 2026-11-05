---
search:
  exclude: true
---

# om3-mom6-single-column: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [om3-mom6-single-column](../om3-mom6-single-column.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

<pre class="paramdoc"><span id="L1">! This file was written by the model and records all non-layout or debugging parameters used at run-time.</span>
<span id="L2"></span>
<span id="L3">! === module MOM ===</span>
<span id="L4">SPLIT = True                    !   [Boolean] default = True</span>
<span id="L5">                                ! Use the split time stepping if true.</span>
<span id="L6">SPLIT_RK2B = False              !   [Boolean] default = False</span>
<span id="L7">                                ! If true, use a version of the split explicit time stepping scheme that</span>
<span id="L8">                                ! exchanges velocities with step_MOM that have the average barotropic phase over</span>
<span id="L9">                                ! a baroclinic timestep rather than the instantaneous barotropic phase.</span>
<span id="L10">CALC_RHO_FOR_SEA_LEVEL = False  !   [Boolean] default = False</span>
<span id="L11">                                ! If true, the in-situ density is used to calculate the effective sea level that</span>
<span id="L12">                                ! is returned to the coupler. If false, the Boussinesq parameter RHO_0 is used.</span>
<span id="L13">ENABLE_THERMODYNAMICS = True    !   [Boolean] default = True</span>
<span id="L14">                                ! If true, Temperature and salinity are used as state variables.</span>
<span id="L15">USE_EOS = True                  !   [Boolean] default = True</span>
<span id="L16">                                ! If true,  density is calculated from temperature and salinity with an equation</span>
<span id="L17">                                ! of state.  If USE_EOS is true, ENABLE_THERMODYNAMICS must be true as well.</span>
<span id="L18">DIABATIC_FIRST = False          !   [Boolean] default = False</span>
<span id="L19">                                ! If true, apply diabatic and thermodynamic processes, including buoyancy</span>
<span id="L20">                                ! forcing and mass gain or loss, before stepping the dynamics forward.</span>
<span id="L21">USE_CONTEMP_ABSSAL = True       !   [Boolean] default = False</span>
<span id="L22">                                ! If true, the prognostics T&amp;S are the conservative temperature and absolute</span>
<span id="L23">                                ! salinity. Care should be taken to convert them to potential temperature and</span>
<span id="L24">                                ! practical salinity before exchanging them with the coupler and/or reporting</span>
<span id="L25">                                ! T&amp;S diagnostics.</span>
<span id="L26">ADIABATIC = False               !   [Boolean] default = False</span>
<span id="L27">                                ! There are no diapycnal mass fluxes if ADIABATIC is true.  This assumes that KD</span>
<span id="L28">                                ! = 0.0 and that there is no buoyancy forcing, but makes the model faster by</span>
<span id="L29">                                ! eliminating subroutine calls.</span>
<span id="L30">DO_DYNAMICS = True              !   [Boolean] default = True</span>
<span id="L31">                                ! If False, skips the dynamics calls that update u &amp; v, as well as the gravity</span>
<span id="L32">                                ! wave adjustment to h. This may be a fragile feature, but can be useful during</span>
<span id="L33">                                ! development</span>
<span id="L34">OFFLINE_TRACER_MODE = False     !   [Boolean] default = False</span>
<span id="L35">                                ! If true, barotropic and baroclinic dynamics, thermodynamics are all bypassed</span>
<span id="L36">                                ! with all the fields necessary to integrate the tracer advection and diffusion</span>
<span id="L37">                                ! equation are read in from files stored from a previous integration of the</span>
<span id="L38">                                ! prognostic model. NOTE: This option only used in the ocean_solo_driver.</span>
<span id="L39">USE_REGRIDDING = True           !   [Boolean] default = False</span>
<span id="L40">                                ! If True, use the ALE algorithm (regridding/remapping). If False, use the</span>
<span id="L41">                                ! layered isopycnal algorithm.</span>
<span id="L42">REMAP_UV_USING_OLD_ALG = False  !   [Boolean] default = False</span>
<span id="L43">                                ! If true, uses the old remapping-via-a-delta-z method for remapping u and v. If</span>
<span id="L44">                                ! false, uses the new method that remaps between grids described by an old and</span>
<span id="L45">                                ! new thickness.</span>
<span id="L46">REMAP_AUXILIARY_VARS = False    !   [Boolean] default = False</span>
<span id="L47">                                ! If true, apply ALE remapping to all of the auxiliary 3-dimensional variables</span>
<span id="L48">                                ! that are needed to reproduce across restarts, similarly to what is already</span>
<span id="L49">                                ! being done with the primary state variables.  The default should be changed to</span>
<span id="L50">                                ! true.</span>
<span id="L51">BULKMIXEDLAYER = False          !   [Boolean] default = False</span>
<span id="L52">                                ! If true, use a Kraus-Turner-like bulk mixed layer with transitional buffer</span>
<span id="L53">                                ! layers.  Layers 1 through NKML+NKBL have variable densities. There must be at</span>
<span id="L54">                                ! least NKML+NKBL+1 layers if BULKMIXEDLAYER is true. BULKMIXEDLAYER can not be</span>
<span id="L55">                                ! used with USE_REGRIDDING. The default is influenced by ENABLE_THERMODYNAMICS.</span>
<span id="L56">USE_POROUS_BARRIER = False      !   [Boolean] default = False</span>
<span id="L57">                                ! If true, use porous barrier to constrain the widths and face areas at the</span>
<span id="L58">                                ! edges of the grid cells.</span>
<span id="L59">BATHYMETRY_AT_VEL = False       !   [Boolean] default = False</span>
<span id="L60">                                ! If true, there are separate values for the basin depths at velocity points.</span>
<span id="L61">                                ! Otherwise the effects of topography are entirely determined from thickness</span>
<span id="L62">                                ! points.</span>
<span id="L63">ENABLE_BUGS_BY_DEFAULT = True   !   [Boolean] default = True</span>
<span id="L64">                                ! If true, the defaults for certain recently added bug-fix flags are set to</span>
<span id="L65">                                ! recreate the bugs so that the code can be moved forward without changing</span>
<span id="L66">                                ! answers for existing configurations.  The defaults for groups of bug-fix flags</span>
<span id="L67">                                ! are periodcially changed to correct the bugs, at which point this parameter</span>
<span id="L68">                                ! will no longer be used to set their default.  Setting this to false means that</span>
<span id="L69">                                ! bugs are only used if they are actively selected, but it also means that</span>
<span id="L70">                                ! answers may change when code is updated due to newly found bugs.</span>
<span id="L71">DT = 3600.0                     !   [s]</span>
<span id="L72">                                ! The (baroclinic) dynamics time step.  The time-step that is actually used will</span>
<span id="L73">                                ! be an integer fraction of the forcing time-step (DT_FORCING in ocean-only mode</span>
<span id="L74">                                ! or the coupling timestep in coupled mode.)</span>
<span id="L75">DT_THERM = 3600.0               !   [s] default = 3600.0</span>
<span id="L76">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L77">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L78">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L79">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L80">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L81">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L82">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L83">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L84">                                ! equal to DT_THERM.</span>
<span id="L85">DT_TRACER_ADVECT = 3600.0       !   [s] default = 3600.0</span>
<span id="L86">                                ! The tracer advection time step. Ideally DT_TRACER_ADVECT should be an integer</span>
<span id="L87">                                ! multiple of DT, less than DT_THERM, and less than the forcing or coupling</span>
<span id="L88">                                ! time-step. However, if TRADV_SPANS_COUPLING is true, DT_TRACER_ADVECT can be</span>
<span id="L89">                                ! longer than the coupling timestep. By default DT_TRACER_ADVECT is set to</span>
<span id="L90">                                ! DT_THERM.</span>
<span id="L91">TRADV_SPANS_COUPLING = False    !   [Boolean] default = False</span>
<span id="L92">                                ! If true, the MOM will take tracer advection timesteps that can be longer than</span>
<span id="L93">                                ! the coupling timestep. The actual tracer advection timestep that is used in</span>
<span id="L94">                                ! this case is the largest integer multiple of the coupling timestep that is</span>
<span id="L95">                                ! less than or equal to DT_TRACER_ADVECT.</span>
<span id="L96">THICKNESSDIFFUSE = True         !   [Boolean] default = False</span>
<span id="L97">                                ! If true, isopycnal surfaces are diffused with a Laplacian coefficient of KHTH.</span>
<span id="L98">APPLY_INTERFACE_FILTER = False  !   [Boolean] default = False</span>
<span id="L99">                                ! If true, model interface heights are subjected to a grid-scale dependent</span>
<span id="L100">                                ! spatial smoothing, often with biharmonic filter.</span>
<span id="L101">THICKNESSDIFFUSE_FIRST = True   !   [Boolean] default = False</span>
<span id="L102">                                ! If true, do thickness diffusion or interface height smoothing before dynamics.</span>
<span id="L103">                                ! This is only used if THICKNESSDIFFUSE or APPLY_INTERFACE_FILTER is true.</span>
<span id="L104">HMIX_SFC_PROP = 1.0             !   [m] default = 1.0</span>
<span id="L105">                                ! If BULKMIXEDLAYER is false, HMIX_SFC_PROP is the depth over which to average</span>
<span id="L106">                                ! to find surface properties like SST and SSS or density (but not surface</span>
<span id="L107">                                ! velocities).</span>
<span id="L108">HMIX_UV_SFC_PROP = 0.0          !   [m] default = 0.0</span>
<span id="L109">                                ! If BULKMIXEDLAYER is false, HMIX_UV_SFC_PROP is the depth over which to</span>
<span id="L110">                                ! average to find surface flow properties, SSU, SSV. A non-positive value</span>
<span id="L111">                                ! indicates no averaging.</span>
<span id="L112">HFREEZE = 10.0                  !   [m] default = -1.0</span>
<span id="L113">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L114">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L115">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L116">                                ! computed.</span>
<span id="L117">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L118">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L119">                                ! step, using the specified value at the end of the step.</span>
<span id="L120">DTBT_RESET_PERIOD = 0.0         !   [s] default = 3600.0</span>
<span id="L121">                                ! The period between recalculations of DTBT (if DTBT &lt;= 0). If DTBT_RESET_PERIOD</span>
<span id="L122">                                ! is negative, DTBT is set based only on information available at</span>
<span id="L123">                                ! initialization.  If 0, DTBT will be set every dynamics time step. The default</span>
<span id="L124">                                ! is set by DT_THERM.  This is only used if SPLIT is true.</span>
<span id="L125">FRAZIL = True                   !   [Boolean] default = False</span>
<span id="L126">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L127">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L128">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L129">DO_GEOTHERMAL = False           !   [Boolean] default = False</span>
<span id="L130">                                ! If true, apply geothermal heating.</span>
<span id="L131">BOUND_SALINITY = True           !   [Boolean] default = False</span>
<span id="L132">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L133">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L134">MIN_SALINITY = 0.0              !   [PPT] default = 0.0</span>
<span id="L135">                                ! The minimum value of salinity when BOUND_SALINITY=True.</span>
<span id="L136">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L137">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L138">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L139">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L140">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L141">C_P = 3992.0                    !   [J kg-1 K-1] default = 3991.86795711963</span>
<span id="L142">                                ! The heat capacity of sea water, approximated as a constant. This is only used</span>
<span id="L143">                                ! if ENABLE_THERMODYNAMICS is true. The default value is from the TEOS-10</span>
<span id="L144">                                ! definition of conservative temperature.</span>
<span id="L145">USE_PSURF_IN_EOS = True         !   [Boolean] default = True</span>
<span id="L146">                                ! If true, always include the surface pressure contributions in equation of</span>
<span id="L147">                                ! state calculations.</span>
<span id="L148">P_REF = 2.0E+07                 !   [Pa] default = 2.0E+07</span>
<span id="L149">                                ! The pressure that is used for calculating the coordinate density.  (1 Pa = 1e4</span>
<span id="L150">                                ! dbar, so 2e7 is commonly used.) This is only used if USE_EOS and</span>
<span id="L151">                                ! ENABLE_THERMODYNAMICS are true.</span>
<span id="L152">NONBLOCKING_P_SURF_BUG = True   !   [Boolean] default = True</span>
<span id="L153">                                ! If true, recover a bug in which the non-blocking halo update of the surface</span>
<span id="L154">                                ! pressure is not completed before the halo points of forces%p_surf are copied</span>
<span id="L155">                                ! into tv%p_surf, so that those halo points hold the surface pressure from the</span>
<span id="L156">                                ! previous coupling step, or zeros on the first step after a restart.  This is</span>
<span id="L157">                                ! only used if NONBLOCKING_UPDATES and USE_PSURF_IN_EOS are true</span>
<span id="L158">FIRST_DIRECTION = 0             ! default = 0</span>
<span id="L159">                                ! An integer that indicates which direction goes first in parts of the code that</span>
<span id="L160">                                ! use directionally split updates, with even numbers (or 0) used for x- first</span>
<span id="L161">                                ! and odd numbers used for y-first.</span>
<span id="L162">ALTERNATE_FIRST_DIRECTION = False !   [Boolean] default = False</span>
<span id="L163">                                ! If true, after every dynamic timestep alternate whether the x- or y- direction</span>
<span id="L164">                                ! updates occur first in directionally split parts of the calculation. If this</span>
<span id="L165">                                ! is true, FIRST_DIRECTION applies at the start of a new run or if the next</span>
<span id="L166">                                ! first direction can not be found in the restart file.</span>
<span id="L167">CHECK_BAD_SURFACE_VALS = True   !   [Boolean] default = False</span>
<span id="L168">                                ! If true, check the surface state for ridiculous values.</span>
<span id="L169">BAD_VAL_SSH_MAX = 50.0          !   [m] default = 20.0</span>
<span id="L170">                                ! The value of SSH above which a bad value message is triggered, if</span>
<span id="L171">                                ! CHECK_BAD_SURFACE_VALS is true.</span>
<span id="L172">BAD_VAL_SSS_MAX = 75.0          !   [PPT] default = 45.0</span>
<span id="L173">                                ! The value of SSS above which a bad value message is triggered, if</span>
<span id="L174">                                ! CHECK_BAD_SURFACE_VALS is true.</span>
<span id="L175">BAD_VAL_SST_MAX = 55.0          !   [deg C] default = 45.0</span>
<span id="L176">                                ! The value of SST above which a bad value message is triggered, if</span>
<span id="L177">                                ! CHECK_BAD_SURFACE_VALS is true.</span>
<span id="L178">BAD_VAL_SST_MIN = -3.0          !   [deg C] default = -2.1</span>
<span id="L179">                                ! The value of SST below which a bad value message is triggered, if</span>
<span id="L180">                                ! CHECK_BAD_SURFACE_VALS is true.</span>
<span id="L181">BAD_VAL_COLUMN_THICKNESS = 0.0  !   [m] default = 0.0</span>
<span id="L182">                                ! The value of column thickness below which a bad value message is triggered, if</span>
<span id="L183">                                ! CHECK_BAD_SURFACE_VALS is true.</span>
<span id="L184">DEFAULT_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L185">                                ! This sets the default value for the various _ANSWER_DATE parameters.</span>
<span id="L186">SURFACE_ANSWER_DATE = 99991231  ! default = 99991231</span>
<span id="L187">                                ! The vintage of the expressions for the surface properties.  Values below</span>
<span id="L188">                                ! 20190101 recover the answers from the end of 2018, while higher values use</span>
<span id="L189">                                ! updated and more robust forms of the same expressions.</span>
<span id="L190">SAVE_INITIAL_CONDS = False      !   [Boolean] default = False</span>
<span id="L191">                                ! If true, write the initial conditions to a file given by IC_OUTPUT_FILE.</span>
<span id="L192">IC_OUTPUT_FILE = &quot;MOM_IC&quot;       ! default = &quot;MOM_IC&quot;</span>
<span id="L193">                                ! The file into which to write the initial conditions.</span>
<span id="L194">WRITE_GEOM = 1                  ! default = 1</span>
<span id="L195">                                ! If =0, never write the geometry and vertical grid files. If =1, write the</span>
<span id="L196">                                ! geometry and vertical grid files only for a new simulation. If =2, always</span>
<span id="L197">                                ! write the geometry and vertical grid files. Other values are invalid.</span>
<span id="L198">GEOM_FILE = &quot;ocean_geometry&quot;    ! default = &quot;ocean_geometry&quot;</span>
<span id="L199">                                ! The file into which to write the ocean geometry.</span>
<span id="L200">USE_DBCLIENT = False            !   [Boolean] default = False</span>
<span id="L201">                                ! If true, initialize a client to a remote database that can be used for online</span>
<span id="L202">                                ! analysis and machine-learning inference.</span>
<span id="L203">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L204">                                ! If true, use the particles package.</span>
<span id="L205">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L206">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L207">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L208">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L209">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L210">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L211">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L212">HOMOGENIZE_FORCINGS = True      !   [Boolean] default = False</span>
<span id="L213">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L214">UPDATE_USTAR = False            !   [Boolean] default = False</span>
<span id="L215">                                ! If True, update ustar from homogenized tau when using the HOMOGENIZE_FORCINGS</span>
<span id="L216">                                ! option.  Note that this will not work with a non-zero gustiness factor.</span>
<span id="L217"></span>
<span id="L218">! === module MOM_domains ===</span>
<span id="L219">REENTRANT_X = True              !   [Boolean] default = True</span>
<span id="L220">                                ! If true, the domain is zonally reentrant.</span>
<span id="L221">REENTRANT_Y = True              !   [Boolean] default = False</span>
<span id="L222">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L223">TRIPOLAR_N = False              !   [Boolean] default = False</span>
<span id="L224">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L225">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L226">NIGLOBAL = 2                    !</span>
<span id="L227">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L228">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L229">NJGLOBAL = 2                    !</span>
<span id="L230">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L231">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L232">NIHALO = 2                      ! default = 4</span>
<span id="L233">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L234">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L235">NJHALO = 2                      ! default = 4</span>
<span id="L236">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L237">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L238"></span>
<span id="L239">! === module MOM_hor_index ===</span>
<span id="L240">! Sets the horizontal array index types.</span>
<span id="L241"></span>
<span id="L242">! === module MOM_grid ===</span>
<span id="L243">! Parameters providing information about the lateral grid.</span>
<span id="L244">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L245">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L246"></span>
<span id="L247">! === module MOM_fixed_initialization ===</span>
<span id="L248">INPUTDIR = &quot;./INPUT/&quot;           ! default = &quot;.&quot;</span>
<span id="L249">                                ! The directory in which input files are found.</span>
<span id="L250"></span>
<span id="L251">! === module MOM_grid_init ===</span>
<span id="L252">GRID_CONFIG = &quot;cartesian&quot;       !</span>
<span id="L253">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L254">                                ! grid.  Current options are:</span>
<span id="L255">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L256">                                !              file set by GRID_FILE.</span>
<span id="L257">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L258">                                !     spherical - use a simple spherical grid.</span>
<span id="L259">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L260">AXIS_UNITS = &quot;degrees&quot;          ! default = &quot;degrees&quot;</span>
<span id="L261">                                ! The units for the Cartesian axes. Valid entries are:</span>
<span id="L262">                                !     degrees - degrees of latitude and longitude</span>
<span id="L263">                                !     m or meter(s) - meters</span>
<span id="L264">                                !     k or km or kilometer(s) - kilometers</span>
<span id="L265">SOUTHLAT = 31.2                 !   [degrees]</span>
<span id="L266">                                ! The southern latitude of the domain or the equivalent starting value for the</span>
<span id="L267">                                ! y-axis.</span>
<span id="L268">LENLAT = 1.0                    !   [degrees]</span>
<span id="L269">                                ! The latitudinal or y-direction length of the domain.</span>
<span id="L270">WESTLON = -64.7                 !   [degrees] default = 0.0</span>
<span id="L271">                                ! The western longitude of the domain or the equivalent starting value for the</span>
<span id="L272">                                ! x-axis.</span>
<span id="L273">LENLON = 1.0                    !   [degrees]</span>
<span id="L274">                                ! The longitudinal or x-direction length of the domain.</span>
<span id="L275">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L276">                                ! The radius of the Earth.</span>
<span id="L277">TOPO_CONFIG = &quot;flat&quot;            !</span>
<span id="L278">                                ! This specifies how bathymetry is specified:</span>
<span id="L279">                                !     file - read bathymetric information from the file</span>
<span id="L280">                                !       specified by (TOPO_FILE).</span>
<span id="L281">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L282">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L283">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L284">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L285">                                !       wall at the southern face.</span>
<span id="L286">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L287">                                !       profile in the meridional direction.</span>
<span id="L288">                                !     bbuilder - build topography from list of functions.</span>
<span id="L289">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L290">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L291">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L292">                                !       DOME sill-overflow test case.</span>
<span id="L293">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L294">                                !       ISOMIP test case.</span>
<span id="L295">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L296">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L297">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L298">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L299">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L300">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L301">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L302">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L303">                                !     USER - call a user modified routine.</span>
<span id="L304">MINIMUM_DEPTH = 0.0             !   [m] default = 0.0</span>
<span id="L305">                                ! The minimum depth of the ocean.</span>
<span id="L306">MAXIMUM_DEPTH = 6000.0          !   [m]</span>
<span id="L307">                                ! The maximum depth of the ocean.</span>
<span id="L308"></span>
<span id="L309">! === module MOM_open_boundary ===</span>
<span id="L310">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L311">! if any.</span>
<span id="L312">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L313">                                ! The number of open boundary segments.</span>
<span id="L314">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L315">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L316">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L317">CHANNEL_CONFIG = &quot;none&quot;         ! default = &quot;none&quot;</span>
<span id="L318">                                ! A parameter that determines which set of channels are</span>
<span id="L319">                                ! restricted to specific  widths.  Options are:</span>
<span id="L320">                                !     none - All channels have the grid width.</span>
<span id="L321">                                !     global_1deg - Sets 16 specific channels appropriate</span>
<span id="L322">                                !       for a 1-degree model, as used in CM2G.</span>
<span id="L323">                                !     list - Read the channel locations and widths from a</span>
<span id="L324">                                !       text file, like MOM_channel_list in the MOM_SIS</span>
<span id="L325">                                !       test case.</span>
<span id="L326">                                !     file - Read open face widths everywhere from a</span>
<span id="L327">                                !       NetCDF file on the model grid.</span>
<span id="L328">SUBGRID_TOPO_AT_VEL = False     !   [Boolean] default = False</span>
<span id="L329">                                ! If true, use variables from TOPO_AT_VEL_FILE as parameters for porous barrier.</span>
<span id="L330">ROTATION = &quot;betaplane&quot;          ! default = &quot;2omegasinlat&quot;</span>
<span id="L331">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L332">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L333">                                !       times the sine of latitude.</span>
<span id="L334">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L335">                                !     USER - call a user modified routine.</span>
<span id="L336">F_0 = 7.66358E-05               !   [s-1] default = 0.0</span>
<span id="L337">                                ! The reference value of the Coriolis parameter with the betaplane option.</span>
<span id="L338">BETA = 0.0                      !   [m-1 s-1] default = 0.0</span>
<span id="L339">                                ! The northward gradient of the Coriolis parameter with the betaplane option.</span>
<span id="L340">BETA_LAT_REF = 0.0              !   [degrees] default = 0.0</span>
<span id="L341">                                ! The reference latitude (origin) of the beta-plane</span>
<span id="L342">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L343">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L344">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L345">                                ! arise at the tripolar fold.</span>
<span id="L346"></span>
<span id="L347">! === module MOM_verticalGrid ===</span>
<span id="L348">! Parameters providing information about the vertical grid.</span>
<span id="L349">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L350">                                ! The gravitational acceleration of the Earth.</span>
<span id="L351">RHO_0 = 1035.0                  !   [kg m-3] default = 1035.0</span>
<span id="L352">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L353">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L354">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L355">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L356">                                ! If true, make the Boussinesq approximation.</span>
<span id="L357">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L358">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L359">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L360">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L361">NK = 75                         !   [nondim]</span>
<span id="L362">                                ! The number of model layers.</span>
<span id="L363">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L364">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L365">                                ! production is set to 0.</span>
<span id="L366"></span>
<span id="L367">! === module MOM_tracer_registry ===</span>
<span id="L368"></span>
<span id="L369">! === module MOM_EOS ===</span>
<span id="L370">EQN_OF_STATE = &quot;ROQUET_RHO&quot;     ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L371">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L372">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L373">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L374">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L375">EOS_QUADRATURE = True           !   [Boolean] default = True</span>
<span id="L376">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L377">                                ! density.</span>
<span id="L378">TFREEZE_FORM = &quot;TEOS_POLY&quot;      ! default = &quot;TEOS10&quot;</span>
<span id="L379">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L380">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L381">                                ! &quot;TEOS10&quot;</span>
<span id="L382">TFREEZE_S_IS_PRACS = False      !   [Boolean] default = False</span>
<span id="L383">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L384">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L385">TFREEZE_T_IS_POTT = False       !   [Boolean] default = False</span>
<span id="L386">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L387">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L388">                                ! applied.</span>
<span id="L389"></span>
<span id="L390">! === module MOM_restart ===</span>
<span id="L391">PARALLEL_RESTARTFILES = False   !   [Boolean] default = False</span>
<span id="L392">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L393">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L394">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L395">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L396">                                ! The name-root of the restart file.</span>
<span id="L397">MAX_FIELDS = 100                ! default = 100</span>
<span id="L398">                                ! The maximum number of restart fields that can be used.</span>
<span id="L399">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L400">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L401">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L402">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L403">                                ! checksums will not match and cause crash.</span>
<span id="L404">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L405">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L406">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L407">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L408">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L409">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L410">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L411">USE_FILTER = False              !   [Boolean] default = False</span>
<span id="L412">                                ! If true, use streaming band-pass filters to detect the instantaneous tidal</span>
<span id="L413">                                ! signals in the simulation.</span>
<span id="L414"></span>
<span id="L415">! === module MOM_tracer_flow_control ===</span>
<span id="L416">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L417">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L418">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L419">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L420">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L421">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L422">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L423">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L424">USE_IDEAL_AGE_TRACER = False    !   [Boolean] default = False</span>
<span id="L425">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L426">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L427">                                ! If true, use the MARBL tracer package.</span>
<span id="L428">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L429">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L430">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L431">                                ! If true, use the file dyes tracer package.</span>
<span id="L432">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L433">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L434">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L435">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L436">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L437">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L438">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L439">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L440">USE_generic_tracer = True       !   [Boolean] default = False</span>
<span id="L441">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L442">                                ! MOM_generic_tracer packages.</span>
<span id="L443">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L444">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L445">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L446">                                ! If true, use the boundary impulse tracer.</span>
<span id="L447">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L448">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L449">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L450">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L451"></span>
<span id="L452">! === module register_MOM_generic_tracer ===</span>
<span id="L453">GENERIC_TRACER_IC_FILE = &quot;&quot;     ! default = &quot;&quot;</span>
<span id="L454">                                ! The file in which the generic tracer initial values can be found, or an empty</span>
<span id="L455">                                ! string for internal initialization.</span>
<span id="L456">GENERIC_TRACER_IC_FILE_IS_Z = False !   [Boolean] default = False</span>
<span id="L457">                                ! If true, GENERIC_TRACER_IC_FILE is in depth space, not layer space.</span>
<span id="L458">TRACERS_MAY_REINIT = False      !   [Boolean] default = False</span>
<span id="L459">                                ! If true, tracers may go through the initialization code if they are not found</span>
<span id="L460">                                ! in the restart files.  Otherwise it is a fatal error if tracers are not found</span>
<span id="L461">                                ! in the restart files of a restarted run.</span>
<span id="L462"></span>
<span id="L463">! === module MOM_coord_initialization ===</span>
<span id="L464">COORD_CONFIG = &quot;none&quot;           ! default = &quot;none&quot;</span>
<span id="L465">                                ! This specifies how layers are to be defined:</span>
<span id="L466">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L467">                                !     file - read coordinate information from the file</span>
<span id="L468">                                !       specified by (COORD_FILE).</span>
<span id="L469">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L470">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L471">                                !     linear - linear based on interfaces not layers</span>
<span id="L472">                                !     layer_ref - linear based on layer densities</span>
<span id="L473">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L474">                                !     ts_range - use range of temperature and salinity</span>
<span id="L475">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L476">                                !       and GINT calculate internal densities.</span>
<span id="L477">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L478">                                !       density and GINT calculate internal densities.</span>
<span id="L479">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L480">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L481">                                !     USER - call a user modified routine.</span>
<span id="L482">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L483">                                ! The reduced gravity at the free surface.</span>
<span id="L484">LIGHTEST_DENSITY = 1035.0       !   [kg m-3] default = 1035.0</span>
<span id="L485">                                ! The reference potential density used for layer 1.</span>
<span id="L486">REGRIDDING_COORDINATE_MODE = &quot;ZSTAR&quot; ! default = &quot;LAYER&quot;</span>
<span id="L487">                                ! Coordinate mode for vertical regridding. Choose among the following</span>
<span id="L488">                                ! possibilities:  LAYER - Isopycnal or stacked shallow water layers</span>
<span id="L489">                                !  ZSTAR, Z* - stretched geopotential z*</span>
<span id="L490">                                !  SIGMA_SHELF_ZSTAR - stretched geopotential z* ignoring shelf</span>
<span id="L491">                                !  SIGMA - terrain following coordinates</span>
<span id="L492">                                !  RHO   - continuous isopycnal</span>
<span id="L493">                                !  HYCOM1 - HyCOM-like hybrid coordinate</span>
<span id="L494">                                !  HYBGEN - Hybrid coordinate from the Hycom hybgen code</span>
<span id="L495">                                !  ADAPTIVE - optimize for smooth neutral density surfaces</span>
<span id="L496">REGRIDDING_COORDINATE_UNITS = &quot;m&quot; ! default = &quot;m&quot;</span>
<span id="L497">                                ! Units of the regridding coordinate.</span>
<span id="L498">ALE_COORDINATE_CONFIG = &quot;FILE:ocean_vgrid.nc,interfaces=zeta&quot; ! default = &quot;UNIFORM&quot;</span>
<span id="L499">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L500">                                !  PARAM       - use the vector-parameter ALE_RESOLUTION</span>
<span id="L501">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L502">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L503">                                !                the filename and variable name, separated</span>
<span id="L504">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L505">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L506">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L507">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L508">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L509">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L510">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L511">                                !                the filename and two variable names, separated</span>
<span id="L512">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L513">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L514">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L515">                                !                the filename and two 3D variable names, separated</span>
<span id="L516">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L517">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L518">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L519">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L520">                                !                the filename and three variable names, separated</span>
<span id="L521">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L522">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L523">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L524">                                !                Map typically contains integer values, but it can</span>
<span id="L525">                                !                contain real values, I+w, which imply using</span>
<span id="L526">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L527">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L528">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L529">!ALE_RESOLUTION = 1.0825614929199219, 1.1963462829589844, 1.322089672088623, 1.4610481262207031, 1.614609718322754, 1.784308910369873, 1.9718408584594727, 2.1790781021118164, 2.4080896377563477, 2.661160469055176, 2.940814971923828, 3.249845504760742, 3.591329574584961, 3.968667984008789, 4.385614395141602, 4.846321105957031, 5.355350494384766, 5.917766571044922, 6.539115905761719, 7.225547790527344, 7.983818054199219, 8.821372985839844, 9.746376037597656, 10.767845153808594, 11.895652770996094, 13.140586853027344, 14.514511108398438, 16.030319213867188, 17.7020263671875, 19.544876098632812, 21.575271606445312, 23.810821533203125, 26.270294189453125, 28.973419189453125, 31.94091796875, 35.194000244140625, 38.75390625, 42.641632080078125, 46.876739501953125, 51.476593017578125, 56.45489501953125, 61.82025146484375, 67.5743408203125, 73.70965576171875, 80.207763671875, 87.03759765625, 94.1534423828125, 101.4951171875, 108.9879150390625, 116.5452880859375, 124.0714111328125, 131.4671630859375, 138.6346435546875, 145.484130859375, 151.938232421875, 157.93701171875, 163.439697265625, 168.42431640625, 172.8876953125, 176.842041015625, 180.3125, 183.33154296875, 185.938720703125, 188.175048828125, 190.08251953125, 191.701171875</span>
<span id="L530">MIN_THICKNESS = 0.001           !   [m] default = 0.001</span>
<span id="L531">                                ! When regridding, this is the minimum layer thickness allowed.</span>
<span id="L532">REMAPPING_SCHEME = &quot;PPM_H4&quot;     ! default = &quot;PLM&quot;</span>
<span id="L533">                                ! This sets the reconstruction scheme used for vertical remapping for all</span>
<span id="L534">                                ! variables. It can be one of the following schemes:</span>
<span id="L535">                                ! PCM         (1st-order accurate)</span>
<span id="L536">                                ! PLM         (2nd-order accurate)</span>
<span id="L537">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L538">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L539">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L540">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L541">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L542">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L543">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L544">VELOCITY_REMAPPING_SCHEME = &quot;PPM_H4&quot; ! default = &quot;PPM_H4&quot;</span>
<span id="L545">                                ! This sets the reconstruction scheme used for vertical remapping of velocities.</span>
<span id="L546">                                ! By default it is the same as REMAPPING_SCHEME. It can be one of the following</span>
<span id="L547">                                ! schemes:</span>
<span id="L548">                                ! PCM         (1st-order accurate)</span>
<span id="L549">                                ! PLM         (2nd-order accurate)</span>
<span id="L550">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L551">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L552">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L553">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L554">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L555">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L556">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L557">FATAL_CHECK_RECONSTRUCTIONS = False !   [Boolean] default = False</span>
<span id="L558">                                ! If true, cell-by-cell reconstructions are checked for consistency and if</span>
<span id="L559">                                ! non-monotonicity or an inconsistency is detected then a FATAL error is issued.</span>
<span id="L560">FATAL_CHECK_REMAPPING = False   !   [Boolean] default = False</span>
<span id="L561">                                ! If true, the results of remapping are checked for conservation and new extrema</span>
<span id="L562">                                ! and if an inconsistency is detected then a FATAL error is issued.</span>
<span id="L563">REMAP_BOUND_INTERMEDIATE_VALUES = False !   [Boolean] default = False</span>
<span id="L564">                                ! If true, the values on the intermediate grid used for remapping are forced to</span>
<span id="L565">                                ! be bounded, which might not be the case due to round off.</span>
<span id="L566">REMAP_BOUNDARY_EXTRAP = False   !   [Boolean] default = False</span>
<span id="L567">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L568">                                ! of piecewise constant</span>
<span id="L569">INIT_BOUNDARY_EXTRAP = False    !   [Boolean] default = False</span>
<span id="L570">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L571">                                ! of piecewise constant during initialization.Defaults to REMAP_BOUNDARY_EXTRAP.</span>
<span id="L572">REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = True</span>
<span id="L573">                                ! This selects the remapping algorithm used in OM4 that does not use the full</span>
<span id="L574">                                ! reconstruction for the top- and lower-most sub-layers, but instead assumes</span>
<span id="L575">                                ! they are always vanished (untrue) and so just uses their edge values. We</span>
<span id="L576">                                ! recommend setting this option to false.</span>
<span id="L577">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L578">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L579">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L580">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L581">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L582">PARTIAL_CELL_VELOCITY_REMAP = False !   [Boolean] default = False</span>
<span id="L583">                                ! If true, use partial cell thicknesses at velocity points that are masked out</span>
<span id="L584">                                ! where they extend below the shallower of the neighboring bathymetry for</span>
<span id="L585">                                ! remapping velocity.</span>
<span id="L586">REMAP_AFTER_INITIALIZATION = True !   [Boolean] default = True</span>
<span id="L587">                                ! If true, applies regridding and remapping immediately after initialization so</span>
<span id="L588">                                ! that the state is ALE consistent. This is a legacy step and should not be</span>
<span id="L589">                                ! needed if the initialization is consistent with the coordinate mode.</span>
<span id="L590">REGRID_TIME_SCALE = 0.0         !   [s] default = 0.0</span>
<span id="L591">                                ! The time-scale used in blending between the current (old) grid and the target</span>
<span id="L592">                                ! (new) grid. A short time-scale favors the target grid (0. or anything less</span>
<span id="L593">                                ! than DT_THERM) has no memory of the old grid. A very long time-scale makes the</span>
<span id="L594">                                ! model more Lagrangian.</span>
<span id="L595">REGRID_FILTER_SHALLOW_DEPTH = 0.0 !   [m] default = 0.0</span>
<span id="L596">                                ! The depth above which no time-filtering is applied. Above this depth final</span>
<span id="L597">                                ! grid exactly matches the target (new) grid.</span>
<span id="L598">REGRID_FILTER_DEEP_DEPTH = 0.0  !   [m] default = 0.0</span>
<span id="L599">                                ! The depth below which full time-filtering is applied with time-scale</span>
<span id="L600">                                ! REGRID_TIME_SCALE. Between depths REGRID_FILTER_SHALLOW_DEPTH and</span>
<span id="L601">                                ! REGRID_FILTER_SHALLOW_DEPTH the filter weights adopt a cubic profile.</span>
<span id="L602">REMAP_VEL_MASK_BBL_THICK = -0.001 !   [m] default = -0.001</span>
<span id="L603">                                ! A thickness of a bottom boundary layer below which velocities in thin layers</span>
<span id="L604">                                ! are zeroed out after remapping, following practice with Hybgen remapping, or a</span>
<span id="L605">                                ! negative value to avoid such filtering altogether.</span>
<span id="L606">REMAP_VEL_CONSERVE_KE = False   !   [Boolean] default = False</span>
<span id="L607">                                ! If true, a correction is applied to the baroclinic component of velocity after</span>
<span id="L608">                                ! remapping so that total KE is conserved. KE may not be conserved when</span>
<span id="L609">                                ! (CS%BBL_h_vel_mask &gt; 0.0) .and. (CS%h_vel_mask &gt; 0.0)</span>
<span id="L610"></span>
<span id="L611">! === module MOM_state_initialization ===</span>
<span id="L612">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L613">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L614">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L615">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L616">INIT_LAYERS_FROM_Z_FILE = True  !   [Boolean] default = False</span>
<span id="L617">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L618">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L619"></span>
<span id="L620">! === module MOM_initialize_layers_from_Z ===</span>
<span id="L621">TEMP_SALT_Z_INIT_FILE = &quot;woa23_ts_01_mom.nc&quot; ! default = &quot;temp_salt_z.nc&quot;</span>
<span id="L622">                                ! The name of the z-space input file used to initialize temperatures (T) and</span>
<span id="L623">                                ! salinities (S). If T and S are not in the same file, TEMP_Z_INIT_FILE and</span>
<span id="L624">                                ! SALT_Z_INIT_FILE must be set.</span>
<span id="L625">TEMP_Z_INIT_FILE = &quot;woa23_ts_01_mom.nc&quot; ! default = &quot;woa23_ts_01_mom.nc&quot;</span>
<span id="L626">                                ! The name of the z-space input file used to initialize temperatures, only.</span>
<span id="L627">SALT_Z_INIT_FILE = &quot;woa23_ts_01_mom.nc&quot; ! default = &quot;woa23_ts_01_mom.nc&quot;</span>
<span id="L628">                                ! The name of the z-space input file used to initialize temperatures, only.</span>
<span id="L629">Z_INIT_FILE_PTEMP_VAR = &quot;ptemp&quot; ! default = &quot;ptemp&quot;</span>
<span id="L630">                                ! The name of the potential temperature variable in TEMP_Z_INIT_FILE.</span>
<span id="L631">Z_INIT_FILE_SALT_VAR = &quot;salt&quot;   ! default = &quot;salt&quot;</span>
<span id="L632">                                ! The name of the salinity variable in SALT_Z_INIT_FILE.</span>
<span id="L633">Z_INIT_HOMOGENIZE = True        !   [Boolean] default = False</span>
<span id="L634">                                ! If True, then horizontally homogenize the interpolated initial conditions.</span>
<span id="L635">Z_INIT_ALE_REMAPPING = True     !   [Boolean] default = False</span>
<span id="L636">                                ! If True, then remap straight to model coordinate from file.</span>
<span id="L637">Z_INIT_REMAPPING_SCHEME = &quot;PPM_IH4&quot; ! default = &quot;PPM_IH4&quot;</span>
<span id="L638">                                ! The remapping scheme to use if using Z_INIT_ALE_REMAPPING is True.</span>
<span id="L639">Z_INIT_REMAP_GENERAL = True     !   [Boolean] default = False</span>
<span id="L640">                                ! If false, only initializes to z* coordinates. If true, allows initialization</span>
<span id="L641">                                ! directly to general coordinates.</span>
<span id="L642">Z_INIT_REMAP_FULL_COLUMN = True !   [Boolean] default = True</span>
<span id="L643">                                ! If false, only reconstructs profiles for valid data points. If true, inserts</span>
<span id="L644">                                ! vanished layers below the valid data.</span>
<span id="L645">Z_INIT_REMAP_OLD_ALG = False    !   [Boolean] default = False</span>
<span id="L646">                                ! If false, uses the preferred remapping algorithm for initialization. If true,</span>
<span id="L647">                                ! use an older, less robust algorithm for remapping.</span>
<span id="L648">TEMP_SALT_INIT_VERTICAL_REMAP_ONLY = False !   [Boolean] default = False</span>
<span id="L649">                                ! If true, initial conditions are on the model horizontal grid. Extrapolation</span>
<span id="L650">                                ! over missing ocean values is done using an ICE-9 procedure with vertical ALE</span>
<span id="L651">                                ! remapping .</span>
<span id="L652">Z_INIT_REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = False</span>
<span id="L653">                                ! If true, use the OM4 remapping-via-subcells algorithm for initialization. See</span>
<span id="L654">                                ! REMAPPING_USE_OM4_SUBCELLS for more details. We recommend setting this option</span>
<span id="L655">                                ! to false.</span>
<span id="L656">HOR_REGRID_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L657">                                ! The vintage of the order of arithmetic for horizontal regridding.  Dates</span>
<span id="L658">                                ! before 20190101 give the same answers as the code did in late 2018, while</span>
<span id="L659">                                ! later versions add parentheses for rotational symmetry.  Dates after 20230101</span>
<span id="L660">                                ! use reproducing sums for global averages.</span>
<span id="L661">LAND_FILL_TEMP = 0.0            !   [degC] default = 0.0</span>
<span id="L662">                                ! A value to use to fill in ocean temperatures on land points.</span>
<span id="L663">LAND_FILL_SALIN = 35.0          !   [ppt] default = 35.0</span>
<span id="L664">                                ! A value to use to fill in ocean salinities on land points.</span>
<span id="L665">HORIZ_INTERP_TOL_TEMP = 0.001   !   [degC] default = 0.001</span>
<span id="L666">                                ! The tolerance in temperature changes between iterations when interpolating</span>
<span id="L667">                                ! from an input dataset using horiz_interp_and_extrap_tracer.  This routine</span>
<span id="L668">                                ! converges slowly, so an overly small tolerance can get expensive.</span>
<span id="L669">HORIZ_INTERP_TOL_SALIN = 0.001  !   [ppt] default = 0.001</span>
<span id="L670">                                ! The tolerance in salinity changes between iterations when interpolating from</span>
<span id="L671">                                ! an input dataset using horiz_interp_and_extrap_tracer.  This routine converges</span>
<span id="L672">                                ! slowly, so an overly small tolerance can get expensive.</span>
<span id="L673">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L674">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L675">                                ! surface pressure is applied.</span>
<span id="L676">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L677">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L678">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L679">                                ! read from file.</span>
<span id="L680">REGRID_ACCELERATE_INIT = False  !   [Boolean] default = False</span>
<span id="L681">                                ! If true, runs REGRID_ACCELERATE_ITERATIONS iterations of the regridding</span>
<span id="L682">                                ! algorithm to push the initial grid to be consistent with the initial</span>
<span id="L683">                                ! condition. Useful only for state-based and iterative coordinates.</span>
<span id="L684">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L685">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L686">                                ! run:</span>
<span id="L687">                                !     file - read velocities from the file specified</span>
<span id="L688">                                !       by (VELOCITY_FILE).</span>
<span id="L689">                                !     zero - the fluid is initially at rest.</span>
<span id="L690">                                !     uniform - the flow is uniform (determined by</span>
<span id="L691">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L692">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L693">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L694">                                !     USER - call a user modified routine.</span>
<span id="L695">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L696">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L697">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L698">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L699">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L700"></span>
<span id="L701">! === module MOM_diag_mediator ===</span>
<span id="L702">NUM_DIAG_COORDS = 2             ! default = 1</span>
<span id="L703">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L704">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L705">DIAG_REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = False</span>
<span id="L706">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L707">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L708">                                ! false.</span>
<span id="L709">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L710">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L711">DIAG_COORDS = &quot;z Z ZSTAR&quot;, &quot;rho2 RHO2 RHO&quot; !</span>
<span id="L712">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L713">                                ! definition used for diagnostics. Each string is of the form</span>
<span id="L714">                                ! &quot;MODULE_SUFFIX,PARAMETER_SUFFIX,COORDINATE_NAME&quot;.</span>
<span id="L715">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L716">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L717">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L718">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L719">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L720">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L721">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L722">                                ! be included in a diag_table.</span>
<span id="L723">DIAG_COORD_DEF_Z = &quot;FILE:ocean_vgrid.nc,interfaces=zeta&quot; ! default = &quot;WOA09&quot;</span>
<span id="L724">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L725">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L726">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L727">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L728">                                !                the filename and variable name, separated</span>
<span id="L729">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L730">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L731">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L732">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L733">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L734">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L735">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L736">                                !                the filename and two variable names, separated</span>
<span id="L737">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L738">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L739">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L740">                                !                the filename and two 3D variable names, separated</span>
<span id="L741">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L742">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L743">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L744">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L745">                                !                the filename and three variable names, separated</span>
<span id="L746">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L747">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L748">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L749">                                !                Map typically contains integer values, but it can</span>
<span id="L750">                                !                contain real values, I+w, which imply using</span>
<span id="L751">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L752">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L753">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L754">DIAG_COORD_INTERP_SCHEME_RHO2 = &quot;PPM_H4&quot; ! default = &quot;PPM_H4&quot;</span>
<span id="L755">                                ! This sets the interpolation scheme to use to determine the new grid. These</span>
<span id="L756">                                ! parameters are only relevant when REGRIDDING_COORDINATE_MODE is set to a</span>
<span id="L757">                                ! function of state. Otherwise, it is not used. It can be one of the following</span>
<span id="L758">                                ! schemes:</span>
<span id="L759">                                !  P1M_H2     (2nd-order accurate)</span>
<span id="L760">                                !  P1M_H4     (2nd-order accurate)</span>
<span id="L761">                                !  P1M_IH4    (2nd-order accurate)</span>
<span id="L762">                                !  PLM        (2nd-order accurate)</span>
<span id="L763">                                !  PPM_CW     (3rd-order accurate)</span>
<span id="L764">                                !  PPM_H4     (3rd-order accurate)</span>
<span id="L765">                                !  PPM_IH4    (3rd-order accurate)</span>
<span id="L766">                                !  P3M_IH4IH3 (4th-order accurate)</span>
<span id="L767">                                !  P3M_IH6IH5 (4th-order accurate)</span>
<span id="L768">                                !  PQM_IH4IH3 (4th-order accurate)</span>
<span id="L769">                                !  PQM_IH6IH5 (5th-order accurate)</span>
<span id="L770">REGRIDDING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L771">                                ! The vintage of the expressions and order of arithmetic to use for regridding.</span>
<span id="L772">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L773">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L774">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L775">DIAG_COORD_DEF_RHO2 = &quot;RFNC1:76,999.5,1020.,1034.1,3.1,1041.,0.002&quot; ! default = &quot;WOA09&quot;</span>
<span id="L776">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L777">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_RHO2</span>
<span id="L778">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L779">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L780">                                !                the filename and variable name, separated</span>
<span id="L781">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L782">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L783">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L784">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L785">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L786">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L787">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L788">                                !                the filename and two variable names, separated</span>
<span id="L789">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L790">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L791">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L792">                                !                the filename and two 3D variable names, separated</span>
<span id="L793">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L794">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L795">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L796">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L797">                                !                the filename and three variable names, separated</span>
<span id="L798">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L799">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L800">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L801">                                !                Map typically contains integer values, but it can</span>
<span id="L802">                                !                contain real values, I+w, which imply using</span>
<span id="L803">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L804">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L805">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L806">DIAG_COORD_P_REF_RHO2 = 2.0E+07 !   [Pa] default = 2.0E+07</span>
<span id="L807">                                ! The pressure that is used for calculating the diagnostic coordinate density.</span>
<span id="L808">                                ! (1 Pa = 1e4 dbar, so 2e7 is commonly used.) This is only used for the RHO</span>
<span id="L809">                                ! coordinate.</span>
<span id="L810">DIAG_COORD_REGRID_COMPRESSIBILITY_FRACTION_RHO2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L811">                                ! When interpolating potential density profiles we can add some artificial</span>
<span id="L812">                                ! compressibility solely to make homogeneous regions appear stratified.</span>
<span id="L813"></span>
<span id="L814">! === module MOM_MEKE ===</span>
<span id="L815">USE_MEKE = True                 !   [Boolean] default = False</span>
<span id="L816">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L817">                                ! kinetic energy budget.</span>
<span id="L818">MEKE_IN_DYNAMICS = True         !   [Boolean] default = True</span>
<span id="L819">                                ! If true, step MEKE forward with the dynamicsotherwise with the tracer</span>
<span id="L820">                                ! timestep.</span>
<span id="L821">EKE_SOURCE = &quot;prog&quot;             ! default = &quot;prog&quot;</span>
<span id="L822">                                ! Determine the where EKE comes from:</span>
<span id="L823">                                !   &#x27;prog&#x27;: Calculated solving EKE equation</span>
<span id="L824">                                !   &#x27;file&#x27;: Read in from a file</span>
<span id="L825">                                !   &#x27;dbclient&#x27;: Retrieved from ML-database</span>
<span id="L826">MEKE_DAMPING = 0.0              !   [s-1] default = 0.0</span>
<span id="L827">                                ! The local depth-independent MEKE dissipation rate.</span>
<span id="L828">MEKE_CD_SCALE = 0.0             !   [nondim] default = 0.0</span>
<span id="L829">                                ! The ratio of the bottom eddy velocity to the column mean eddy velocity, i.e.</span>
<span id="L830">                                ! sqrt(2*MEKE). This should be less than 1 to account for the surface</span>
<span id="L831">                                ! intensification of MEKE.</span>
<span id="L832">MEKE_CB = 25.0                  !   [nondim] default = 25.0</span>
<span id="L833">                                ! A coefficient in the expression for the ratio of bottom projected eddy energy</span>
<span id="L834">                                ! and mean column energy (see Jansen et al. 2015).</span>
<span id="L835">MEKE_MIN_GAMMA2 = 1.0E-04       !   [nondim] default = 1.0E-04</span>
<span id="L836">                                ! The minimum allowed value of gamma_b^2.</span>
<span id="L837">MEKE_CT = 50.0                  !   [nondim] default = 50.0</span>
<span id="L838">                                ! A coefficient in the expression for the ratio of barotropic eddy energy and</span>
<span id="L839">                                ! mean column energy (see Jansen et al. 2015).</span>
<span id="L840">MEKE_GMCOEFF = 1.0              !   [nondim] default = -1.0</span>
<span id="L841">                                ! The efficiency of the conversion of potential energy into MEKE by the</span>
<span id="L842">                                ! thickness mixing parameterization. If MEKE_GMCOEFF is negative, this</span>
<span id="L843">                                ! conversion is not used or calculated.</span>
<span id="L844">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L845">                                ! If MEKE_GEOMETRIC is true, uses the GM coefficient formulation from the</span>
<span id="L846">                                ! GEOMETRIC framework (Marshall et al., 2012).</span>
<span id="L847">MEKE_GEOMETRIC_ALPHA = 0.05     !   [nondim] default = 0.05</span>
<span id="L848">                                ! The nondimensional coefficient governing the efficiency of the GEOMETRIC</span>
<span id="L849">                                ! thickness diffusion.</span>
<span id="L850">MEKE_EQUILIBRIUM_ALT = False    !   [Boolean] default = False</span>
<span id="L851">                                ! If true, use an alternative formula for computing the (equilibrium)initial</span>
<span id="L852">                                ! value of MEKE.</span>
<span id="L853">MEKE_EQUILIBRIUM_RESTORING = False !   [Boolean] default = False</span>
<span id="L854">                                ! If true, restore MEKE back to its equilibrium value, which is calculated at</span>
<span id="L855">                                ! each time step.</span>
<span id="L856">MEKE_FRCOEFF = -1.0             !   [nondim] default = -1.0</span>
<span id="L857">                                ! The efficiency of the conversion of mean energy into MEKE.  If MEKE_FRCOEFF is</span>
<span id="L858">                                ! negative, this conversion is not used or calculated.</span>
<span id="L859">MEKE_BHFRCOEFF = -1.0           !   [nondim] default = -1.0</span>
<span id="L860">                                ! The efficiency of the conversion of mean energy into MEKE by the biharmonic</span>
<span id="L861">                                ! dissipation.  If MEKE_bhFRCOEFF is negative, this conversion is not used or</span>
<span id="L862">                                ! calculated.</span>
<span id="L863">MEKE_GMECOEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L864">                                ! The efficiency of the conversion of MEKE into mean energy by GME.  If</span>
<span id="L865">                                ! MEKE_GMECOEFF is negative, this conversion is not used or calculated.</span>
<span id="L866">MEKE_BGSRC = 1.0E-13            !   [W kg-1] default = 0.0</span>
<span id="L867">                                ! A background energy source for MEKE.</span>
<span id="L868">MEKE_KH = -1.0                  !   [m2 s-1] default = -1.0</span>
<span id="L869">                                ! A background lateral diffusivity of MEKE. Use a negative value to not apply</span>
<span id="L870">                                ! lateral diffusion to MEKE.</span>
<span id="L871">MEKE_K4 = -1.0                  !   [m4 s-1] default = -1.0</span>
<span id="L872">                                ! A lateral bi-harmonic diffusivity of MEKE. Use a negative value to not apply</span>
<span id="L873">                                ! bi-harmonic diffusion to MEKE.</span>
<span id="L874">MEKE_DTSCALE = 1.0              !   [nondim] default = 1.0</span>
<span id="L875">                                ! A scaling factor to accelerate the time evolution of MEKE.</span>
<span id="L876">MEKE_POSITIVE = False           !   [Boolean] default = False</span>
<span id="L877">                                ! If true, it guarantees that MEKE will always be &gt;= 0.</span>
<span id="L878">MEKE_KHCOEFF = 1.0              !   [nondim] default = 1.0</span>
<span id="L879">                                ! A scaling factor in the expression for eddy diffusivity which is otherwise</span>
<span id="L880">                                ! proportional to the MEKE velocity- scale times an eddy mixing-length. This</span>
<span id="L881">                                ! factor must be &gt;0 for MEKE to contribute to the thickness/ and tracer</span>
<span id="L882">                                ! diffusivity in the rest of the model.</span>
<span id="L883">MEKE_USCALE = 0.0               !   [m s-1] default = 0.0</span>
<span id="L884">                                ! The background velocity that is combined with MEKE to calculate the bottom</span>
<span id="L885">                                ! drag.</span>
<span id="L886">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L887">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L888">                                ! streamfunction for the MEKE GM source term.</span>
<span id="L889">MEKE_VISC_DRAG = True           !   [Boolean] default = True</span>
<span id="L890">                                ! If true, use the vertvisc_type to calculate the bottom drag acting on MEKE.</span>
<span id="L891">MEKE_KHTH_FAC = 0.3             !   [nondim] default = 0.0</span>
<span id="L892">                                ! A factor that maps MEKE%Kh to KhTh.</span>
<span id="L893">MEKE_KHTR_FAC = 0.3             !   [nondim] default = 0.0</span>
<span id="L894">                                ! A factor that maps MEKE%Kh to KhTr.</span>
<span id="L895">MEKE_KHMEKE_FAC = 1.0           !   [nondim] default = 0.0</span>
<span id="L896">                                ! A factor that maps MEKE%Kh to Kh for MEKE itself.</span>
<span id="L897">MEKE_OLD_LSCALE = False         !   [Boolean] default = False</span>
<span id="L898">                                ! If true, use the old formula for length scale which is a function of grid</span>
<span id="L899">                                ! spacing and deformation radius.</span>
<span id="L900">MEKE_MIN_LSCALE = False         !   [Boolean] default = False</span>
<span id="L901">                                ! If true, use a strict minimum of provided length scales rather than harmonic</span>
<span id="L902">                                ! mean.</span>
<span id="L903">MEKE_RD_MAX_SCALE = False       !   [Boolean] default = False</span>
<span id="L904">                                ! If true, the length scale used by MEKE is the minimum of the deformation</span>
<span id="L905">                                ! radius or grid-spacing. Only used if MEKE_OLD_LSCALE=True</span>
<span id="L906">MEKE_VISCOSITY_COEFF_KU = 0.6   !   [nondim] default = 0.0</span>
<span id="L907">                                ! If non-zero, is the scaling coefficient in the expression forviscosity used to</span>
<span id="L908">                                ! parameterize harmonic lateral momentum mixing byunresolved eddies represented</span>
<span id="L909">                                ! by MEKE. Can be negative torepresent backscatter from the unresolved eddies.</span>
<span id="L910">MEKE_VISCOSITY_COEFF_AU = 0.0   !   [nondim] default = 0.0</span>
<span id="L911">                                ! If non-zero, is the scaling coefficient in the expression forviscosity used to</span>
<span id="L912">                                ! parameterize biharmonic lateral momentum mixing byunresolved eddies</span>
<span id="L913">                                ! represented by MEKE. Can be negative torepresent backscatter from the</span>
<span id="L914">                                ! unresolved eddies.</span>
<span id="L915">MEKE_FIXED_MIXING_LENGTH = 0.0  !   [m] default = 0.0</span>
<span id="L916">                                ! If positive, is a fixed length contribution to the expression for mixing</span>
<span id="L917">                                ! length used in MEKE-derived diffusivity.</span>
<span id="L918">MEKE_FIXED_TOTAL_DEPTH = True   !   [Boolean] default = True</span>
<span id="L919">                                ! If true, use the nominal bathymetric depth as the estimate of the time-varying</span>
<span id="L920">                                ! ocean depth.  Otherwise base the depth on the total ocean massper unit area.</span>
<span id="L921">MEKE_ALPHA_DEFORM = 0.0         !   [nondim] default = 0.0</span>
<span id="L922">                                ! If positive, is a coefficient weighting the deformation scale in the</span>
<span id="L923">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L924">MEKE_ALPHA_RHINES = 0.15        !   [nondim] default = 0.0</span>
<span id="L925">                                ! If positive, is a coefficient weighting the Rhines scale in the expression for</span>
<span id="L926">                                ! mixing length used in MEKE-derived diffusivity.</span>
<span id="L927">MEKE_ALPHA_EADY = 0.15          !   [nondim] default = 0.0</span>
<span id="L928">                                ! If positive, is a coefficient weighting the Eady length scale in the</span>
<span id="L929">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L930">MEKE_ALPHA_FRICT = 0.0          !   [nondim] default = 0.0</span>
<span id="L931">                                ! If positive, is a coefficient weighting the frictional arrest scale in the</span>
<span id="L932">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L933">MEKE_ALPHA_GRID = 0.0           !   [nondim] default = 0.0</span>
<span id="L934">                                ! If positive, is a coefficient weighting the grid-spacing as a scale in the</span>
<span id="L935">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L936">MEKE_COLD_START = False         !   [Boolean] default = False</span>
<span id="L937">                                ! If true, initialize EKE to zero. Otherwise a local equilibrium solution is</span>
<span id="L938">                                ! used as an initial condition for EKE.</span>
<span id="L939">MEKE_BACKSCAT_RO_C = 0.0        !   [nondim] default = 0.0</span>
<span id="L940">                                ! The coefficient in the Rossby number function for scaling the biharmonic</span>
<span id="L941">                                ! frictional energy source. Setting to non-zero enables the Rossby number</span>
<span id="L942">                                ! function.</span>
<span id="L943">MEKE_BACKSCAT_RO_POW = 0.0      !   [nondim] default = 0.0</span>
<span id="L944">                                ! The power in the Rossby number function for scaling the biharmonic frictional</span>
<span id="L945">                                ! energy source.</span>
<span id="L946">MEKE_ADVECTION_FACTOR = 0.0     !   [nondim] default = 0.0</span>
<span id="L947">                                ! A scale factor in front of advection of eddy energy. Zero turns advection off.</span>
<span id="L948">                                ! Using unity would be normal but other values could accommodate a mismatch</span>
<span id="L949">                                ! between the advecting barotropic flow and the vertical structure of MEKE.</span>
<span id="L950">MEKE_TOPOGRAPHIC_BETA = 0.0     !   [nondim] default = 0.0</span>
<span id="L951">                                ! A scale factor to determine how much topographic beta is weighed in computing</span>
<span id="L952">                                ! beta in the expression of Rhines scale. Use 1 if full topographic beta effect</span>
<span id="L953">                                ! is considered; use 0 if it&#x27;s completely ignored.</span>
<span id="L954">SQG_USE_MEKE = False            !   [Boolean] default = False</span>
<span id="L955">                                ! If true, the eddy scale of MEKE is used for the SQG vertical structure</span>
<span id="L956">CDRAG = 0.003                   !   [nondim] default = 0.003</span>
<span id="L957">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L958">                                ! the bottom stress.</span>
<span id="L959">MEKE_CDRAG = 0.003              !   [nondim] default = 0.003</span>
<span id="L960">                                ! Drag coefficient relating the magnitude of the velocity field to the bottom</span>
<span id="L961">                                ! stress in MEKE.</span>
<span id="L962"></span>
<span id="L963">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L964">USE_VARIABLE_MIXING = True      !   [Boolean] default = False</span>
<span id="L965">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L966">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L967">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L968">                                ! file.</span>
<span id="L969">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L970">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L971">                                ! thickness diffusivity.</span>
<span id="L972">RESOLN_SCALED_KH = True         !   [Boolean] default = False</span>
<span id="L973">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L974">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L975">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L976">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L977">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L978">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L979">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L980">RESOLN_SCALED_KHTH = True       !   [Boolean] default = False</span>
<span id="L981">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L982">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L983">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L984">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L985">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L986">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L987">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L988">                                ! wave for calculating the resolution fn.</span>
<span id="L989">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L990">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L991">                                ! structure.</span>
<span id="L992">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L993">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L994">                                ! that BS_EBT_power=0</span>
<span id="L995">KHTH_USE_EBT_STRUCT = True      !   [Boolean] default = False</span>
<span id="L996">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L997">                                ! thickness diffusivity.</span>
<span id="L998">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L999">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L1000">                                ! of thickness diffusivity.</span>
<span id="L1001">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1002">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1003">                                ! tracer diffusivity.</span>
<span id="L1004">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1005">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L1006">                                ! of tracer diffusivity.</span>
<span id="L1007">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L1008">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1009">                                ! diffusivity in the GL90 scheme.</span>
<span id="L1010">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L1011">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1012">                                ! diffusivity in the GL90 scheme.</span>
<span id="L1013">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L1014">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L1015">                                ! diffusivity</span>
<span id="L1016">KHTR_SLOPE_CFF = 0.25           !   [nondim] default = 0.0</span>
<span id="L1017">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L1018">                                ! diffusivity</span>
<span id="L1019">USE_STORED_SLOPES = True        !   [Boolean] default = False</span>
<span id="L1020">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L1021">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L1022">                                ! should be necessary.</span>
<span id="L1023">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L1024">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L1025">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L1026">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L1027">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L1028">                                ! code.</span>
<span id="L1029">RESOLN_N2_FILTER_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1030">                                ! The depth below which N2 is monotonized to avoid stratification artifacts from</span>
<span id="L1031">                                ! altering the equivalent barotropic mode structure.  This monotonzization is</span>
<span id="L1032">                                ! disabled if this parameter is negative.</span>
<span id="L1033">VISBECK_MAX_SLOPE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1034">                                ! If non-zero, is an upper bound on slopes used in the Visbeck formula for</span>
<span id="L1035">                                ! diffusivity. This does not affect the isopycnal slope calculation used within</span>
<span id="L1036">                                ! thickness diffusion.</span>
<span id="L1037">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L1038">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L1039">                                ! &amp; S into thin layers.</span>
<span id="L1040">USE_SIMPLER_EADY_GROWTH_RATE = False !   [Boolean] default = False</span>
<span id="L1041">                                ! If true, use a simpler method to calculate the Eady growth rate that avoids</span>
<span id="L1042">                                ! division by layer thickness. Recommended.</span>
<span id="L1043">VARMIX_KTOP = 2                 !   [nondim] default = 2</span>
<span id="L1044">                                ! The layer number at which to start vertical integration of S*N for purposes of</span>
<span id="L1045">                                ! finding the Eady growth rate.</span>
<span id="L1046">VISBECK_L_SCALE = 0.0           !   [m or nondim] default = 0.0</span>
<span id="L1047">                                ! The fixed length scale in the Visbeck formula, or if negative a nondimensional</span>
<span id="L1048">                                ! scaling factor relating this length scale squared to the cell areas.</span>
<span id="L1049">KH_RES_SCALE_COEF = 1.0         !   [nondim] default = 1.0</span>
<span id="L1050">                                ! A coefficient that determines how KhTh is scaled away if RESOLN_SCALED_... is</span>
<span id="L1051">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER).</span>
<span id="L1052">KH_RES_FN_POWER = 3             ! default = 2</span>
<span id="L1053">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L1054">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L1055">                                ! greater than 100 results in a step-function being used.</span>
<span id="L1056">VISC_RES_SCALE_COEF = 1.0       !   [nondim] default = 1.0</span>
<span id="L1057">                                ! A coefficient that determines how Kh is scaled away if RESOLN_SCALED_... is</span>
<span id="L1058">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER). This</span>
<span id="L1059">                                ! function affects lateral viscosity, Kh, and not KhTh.</span>
<span id="L1060">VISC_RES_FN_POWER = 3           ! default = 3</span>
<span id="L1061">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L1062">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L1063">                                ! greater than 100 results in a step-function being used. This function affects</span>
<span id="L1064">                                ! lateral viscosity, Kh, and not KhTh.</span>
<span id="L1065">INTERPOLATE_RES_FN = False      !   [Boolean] default = False</span>
<span id="L1066">                                ! If true, interpolate the resolution function to the velocity points from the</span>
<span id="L1067">                                ! thickness points; otherwise interpolate the wave speed and calculate the</span>
<span id="L1068">                                ! resolution function independently at each point.</span>
<span id="L1069">GILL_EQUATORIAL_LD = True       !   [Boolean] default = True</span>
<span id="L1070">                                ! If true, uses Gill&#x27;s definition of the baroclinic equatorial deformation</span>
<span id="L1071">                                ! radius, otherwise, if false, use Pedlosky&#x27;s definition. These definitions</span>
<span id="L1072">                                ! differ by a factor of 2 in front of the beta term in the denominator. Gill&#x27;s</span>
<span id="L1073">                                ! is the more appropriate definition.</span>
<span id="L1074">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L1075">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L1076">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L1077">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L1078">INTERNAL_WAVE_SPEED_BETTER_EST = True !   [Boolean] default = True</span>
<span id="L1079">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L1080">                                ! starting point for iterations.</span>
<span id="L1081">EBT_REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = False</span>
<span id="L1082">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1083">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1084">                                ! this option to false.</span>
<span id="L1085">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L1086">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L1087"></span>
<span id="L1088">! === module MOM_set_visc ===</span>
<span id="L1089">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1090">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L1091">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1092">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1093">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L1094">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L1095">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L1096">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L1097">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L1098">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L1099">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L1100">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L1101">                                ! layer is HBBL.</span>
<span id="L1102">CHANNEL_DRAG = True             !   [Boolean] default = False</span>
<span id="L1103">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L1104">                                ! fraction of the bottom it overlies.</span>
<span id="L1105">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L1106">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L1107">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L1108">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L1109">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L1110">                                ! thickness for viscosity.</span>
<span id="L1111">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L1112">                                ! The rotation rate of the earth.</span>
<span id="L1113">HBBL = 10.0                     !   [m]</span>
<span id="L1114">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L1115">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L1116">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L1117">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L1118">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L1119">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L1120">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L1121">                                ! and LINEAR_DRAG is false.</span>
<span id="L1122">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L1123">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L1124">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L1125">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L1126">                                ! defined.</span>
<span id="L1127">BBL_USE_EOS = True              !   [Boolean] default = True</span>
<span id="L1128">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L1129">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L1130">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L1131">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L1132">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L1133">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L1134">                                ! near-bottom viscosity.</span>
<span id="L1135">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L1136">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L1137">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L1138">                                ! viscosity.</span>
<span id="L1139">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L1140">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L1141">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L1142">KV = 0.0                        !   [m2 s-1]</span>
<span id="L1143">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L1144">                                ! m2 s-1, may be used.</span>
<span id="L1145">KV_BBL_MIN = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1146">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L1147">KV_TBL_MIN = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1148">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L1149">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L1150">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L1151">                                ! the bottom layer feels the intended drag.</span>
<span id="L1152">SMAG_CONST_CHANNEL = 0.15       !   [nondim] default = 0.15</span>
<span id="L1153">                                ! The nondimensional Laplacian Smagorinsky constant used in calculating the</span>
<span id="L1154">                                ! channel drag if it is enabled.  The default is to use the same value as</span>
<span id="L1155">                                ! SMAG_LAP_CONST if it is defined, or 0.15 if it is not. The value used is also</span>
<span id="L1156">                                ! 0.15 if the specified value is negative.</span>
<span id="L1157">TRIG_CHANNEL_DRAG_WIDTHS = True !   [Boolean] default = True</span>
<span id="L1158">                                ! If true, use trigonometric expressions to determine the fractional open</span>
<span id="L1159">                                ! interface lengths for concave topography.</span>
<span id="L1160">CHANNEL_DRAG_MAX_BBL_THICK = 5.0 !   [m] default = 5.0</span>
<span id="L1161">                                ! The maximum bottom boundary layer thickness over which the channel drag is</span>
<span id="L1162">                                ! exerted, or a negative value for no fixed limit, instead basing the BBL</span>
<span id="L1163">                                ! thickness on the bottom stress, rotation and stratification.  The default is</span>
<span id="L1164">                                ! proportional to HBBL if USE_JACKSON_PARAM or DRAG_AS_BODY_FORCE is true.</span>
<span id="L1165"></span>
<span id="L1166">! === module MOM_thickness_diffuse ===</span>
<span id="L1167">KHTH = 0.0                      !   [m2 s-1] default = 0.0</span>
<span id="L1168">                                ! The background horizontal thickness diffusivity.</span>
<span id="L1169">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L1170">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L1171">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L1172">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1173">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L1174">KHTH_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1175">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L1176">KHTH_MAX_CFL = 0.1              !   [nondimensional] default = 0.8</span>
<span id="L1177">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L1178">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L1179">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L1180">                                ! models.</span>
<span id="L1181">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L1182">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L1183">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L1184">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L1185">                                ! are scaled back proportionately.</span>
<span id="L1186">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L1187">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L1188">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L1189">                                ! the layer density structure).</span>
<span id="L1190">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L1191">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L1192">                                ! horizontally smooth jagged layers.</span>
<span id="L1193">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L1194">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L1195">                                ! scaled away.</span>
<span id="L1196">KHTH_USE_FGNV_STREAMFUNCTION = True !   [Boolean] default = False</span>
<span id="L1197">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L1198">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L1199">FGNV_FILTER_SCALE = 0.1         !   [nondim] default = 1.0</span>
<span id="L1200">                                ! A coefficient scaling the vertical smoothing term in the Ferrari et al., 2010,</span>
<span id="L1201">                                ! streamfunction formulation.</span>
<span id="L1202">FGNV_C_MIN = 0.0                !   [m s-1] default = 0.0</span>
<span id="L1203">                                ! A minium wave speed used in the Ferrari et al., 2010, streamfunction</span>
<span id="L1204">                                ! formulation.</span>
<span id="L1205">FGNV_STRAT_FLOOR = 1.0E-15      !   [nondim] default = 1.0E-15</span>
<span id="L1206">                                ! A floor for Brunt-Vasaila frequency in the Ferrari et al., 2010,</span>
<span id="L1207">                                ! streamfunction formulation, expressed as a fraction of planetary rotation,</span>
<span id="L1208">                                ! OMEGA. This should be tiny but non-zero to avoid degeneracy.</span>
<span id="L1209">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L1210">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L1211">USE_KH_IN_MEKE = False          !   [Boolean] default = False</span>
<span id="L1212">                                ! If true, uses the thickness diffusivity calculated here to diffuse MEKE.</span>
<span id="L1213">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L1214">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L1215">                                ! McWilliams parameterization.</span>
<span id="L1216">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L1217">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L1218">                                ! sign, for legacy reproducibility.</span>
<span id="L1219">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L1220">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L1221">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L1222">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L1223"></span>
<span id="L1224">! === module MOM_dynamics_split_RK2 ===</span>
<span id="L1225">TIDES = False                   !   [Boolean] default = False</span>
<span id="L1226">                                ! If true, apply tidal momentum forcing.</span>
<span id="L1227">CALCULATE_SAL = False           !   [Boolean] default = False</span>
<span id="L1228">                                ! If true, calculate self-attraction and loading.</span>
<span id="L1229">USE_HA = False                  !   [Boolean] default = False</span>
<span id="L1230">                                ! If true, perform inline harmonic analysis.</span>
<span id="L1231">BE = 0.6                        !   [nondim] default = 0.6</span>
<span id="L1232">                                ! If SPLIT is true, BE determines the relative weighting of a  2nd-order</span>
<span id="L1233">                                ! Runga-Kutta baroclinic time stepping scheme (0.5) and a backward Euler scheme</span>
<span id="L1234">                                ! (1) that is used for the Coriolis and inertial terms.  BE may be from 0.5 to</span>
<span id="L1235">                                ! 1, but instability may occur near 0.5. BE is also applicable if SPLIT is false</span>
<span id="L1236">                                ! and USE_RK2 is true.</span>
<span id="L1237">BEGW = 0.0                      !   [nondim] default = 0.0</span>
<span id="L1238">                                ! If SPLIT is true, BEGW is a number from 0 to 1 that controls the extent to</span>
<span id="L1239">                                ! which the treatment of gravity waves is forward-backward (0) or simulated</span>
<span id="L1240">                                ! backward Euler (1).  0 is almost always used. If SPLIT is false and USE_RK2 is</span>
<span id="L1241">                                ! true, BEGW can be between 0 and 0.5 to damp gravity waves.</span>
<span id="L1242">SET_DTBT_USE_BT_CONT = False    !   [Boolean] default = False</span>
<span id="L1243">                                ! If true, use BT_CONT to calculate DTBT if possible.</span>
<span id="L1244">SPLIT_BOTTOM_STRESS = False     !   [Boolean] default = False</span>
<span id="L1245">                                ! If true, provide the bottom stress calculated by the vertical viscosity to the</span>
<span id="L1246">                                ! barotropic solver.</span>
<span id="L1247">BT_USE_LAYER_FLUXES = True      !   [Boolean] default = True</span>
<span id="L1248">                                ! If true, use the summed layered fluxes plus an adjustment due to the change in</span>
<span id="L1249">                                ! the barotropic velocity in the barotropic continuity equation.</span>
<span id="L1250">BT_ADJ_CORR_MASS_SRC = True     !   [Boolean] default = True</span>
<span id="L1251">                                ! If true, recalculates the barotropic mass source after predictor step. This</span>
<span id="L1252">                                ! should make little difference in the deep ocean but appears to help for</span>
<span id="L1253">                                ! vanished layers. If false, uses the same mass source as from the predictor</span>
<span id="L1254">                                ! step.</span>
<span id="L1255">STORE_CORIOLIS_ACCEL = True     !   [Boolean] default = True</span>
<span id="L1256">                                ! If true, calculate the Coriolis accelerations at the end of each timestep for</span>
<span id="L1257">                                ! use in the predictor step of the next split RK2 timestep.</span>
<span id="L1258">FPMIX = False                   !   [Boolean] default = False</span>
<span id="L1259">                                ! If true, add non-local momentum flux increments and diffuse down the Eulerian</span>
<span id="L1260">                                ! gradient.</span>
<span id="L1261">VISC_REM_BUG = False            !   [Boolean] default = False</span>
<span id="L1262">                                ! If true, visc_rem_[uv] in split mode is incorrectly calculated or accounted</span>
<span id="L1263">                                ! for in two places. This parameter controls the defaults of two individual</span>
<span id="L1264">                                ! flags, VISC_REM_TIMESTEP_BUG in MOM_dynamics_split_RK2(b) and</span>
<span id="L1265">                                ! VISC_REM_BT_WEIGHT_BUG in MOM_barotropic.</span>
<span id="L1266">VISC_REM_TIMESTEP_BUG = False   !   [Boolean] default = False</span>
<span id="L1267">                                ! If true, recover a bug that uses dt_pred rather than dt in vertvisc_remnant()</span>
<span id="L1268">                                ! at the end of predictor stage for the following continuity() and btstep()</span>
<span id="L1269">                                ! calls in the corrector step. Default of this flag is set by VISC_REM_BUG</span>
<span id="L1270"></span>
<span id="L1271">! === module MOM_continuity_PPM ===</span>
<span id="L1272">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L1273">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L1274">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L1275">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L1276">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L1277">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L1278">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L1279">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L1280">                                ! of accuracy of the dynamic core.</span>
<span id="L1281">UPWIND_1ST_CONTINUITY = True    !   [Boolean] default = False</span>
<span id="L1282">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L1283">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L1284">                                ! mode where its minimal stencil is useful.</span>
<span id="L1285">ETA_TOLERANCE = 1.0E-06         !   [m] default = 3.75E-09</span>
<span id="L1286">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L1287">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L1288">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L1289">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L1290">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L1291">VELOCITY_TOLERANCE = 1.0E-04    !   [m s-1] default = 3.0E+08</span>
<span id="L1292">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L1293">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L1294">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L1295">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L1296">                                ! 0.5.</span>
<span id="L1297">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L1298">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L1299">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L1300">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L1301">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L1302">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L1303">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L1304">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L1305">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L1306">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L1307">                                ! viscous columns.</span>
<span id="L1308">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L1309">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L1310">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L1311"></span>
<span id="L1312">! === module MOM_CoriolisAdv ===</span>
<span id="L1313">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L1314">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L1315">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L1316">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L1317">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L1318">CORIOLIS_EN_DIS = False         !   [Boolean] default = False</span>
<span id="L1319">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L1320">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L1321">                                ! used.</span>
<span id="L1322">CORIOLIS_SCHEME = &quot;SADOURNY75_ENSTRO&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L1323">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L1324">                                ! values are:</span>
<span id="L1325">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L1326">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L1327">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L1328">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L1329">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L1330">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L1331">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1332">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1333">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1334">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1335">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1336">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1337">                                ! option would have no effect on the SADOURNY Coriolis scheme if it were</span>
<span id="L1338">                                ! possible to use centered difference thickness fluxes.</span>
<span id="L1339">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1340">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1341">                                ! energy gradient. Valid values are:</span>
<span id="L1342">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1343">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1344">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1345">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1346">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1347"></span>
<span id="L1348">! === module MOM_PressureForce ===</span>
<span id="L1349">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1350">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1351">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1352">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1353">                                ! al., O. Mod. (2008).</span>
<span id="L1354"></span>
<span id="L1355">! === module MOM_PressureForce_FV ===</span>
<span id="L1356">RHO_PGF_REF = 1035.0            !   [kg m-3] default = 1035.0</span>
<span id="L1357">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1358">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1359">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1360">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1361">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1362">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1363">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1364">                                ! Boussinesq mode.</span>
<span id="L1365">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L1366">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L1367">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L1368">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L1369">                                ! pressure.</span>
<span id="L1370">MASS_WEIGHT_IN_PRESSURE_GRADIENT = True !   [Boolean] default = False</span>
<span id="L1371">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1372">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1373">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = True !   [Boolean] default = True</span>
<span id="L1374">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1375">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1376">                                ! pressure gradient calculations.</span>
<span id="L1377">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L1378">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1379">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1380">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1381">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1382">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L1383">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1384">                                ! pressure correction.</span>
<span id="L1385">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L1386">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1387">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1388">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1389">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1390">                                ! inaccurate way. This is not recommended.</span>
<span id="L1391">RECONSTRUCT_FOR_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1392">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1393">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1394">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1395">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1396">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1397">                                ! pressure gradient calculation.</span>
<span id="L1398">                                !  0: PCM or no reconstruction.</span>
<span id="L1399">                                !  1: PLM reconstruction.</span>
<span id="L1400">                                !  2: PPM reconstruction.</span>
<span id="L1401">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1402">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1403">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1404">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1405">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1406">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1407"></span>
<span id="L1408">! === module MOM_Zanna_Bolton ===</span>
<span id="L1409">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1410">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1411">                                ! mesoscale eddies.</span>
<span id="L1412"></span>
<span id="L1413">! === module MOM_hor_visc ===</span>
<span id="L1414">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1415">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1416">                                ! Leith)</span>
<span id="L1417">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1418">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1419">                                ! currently only works with split mode.</span>
<span id="L1420">LAPLACIAN = True                !   [Boolean] default = False</span>
<span id="L1421">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1422">KH = 0.0                        !   [m2 s-1] default = 0.0</span>
<span id="L1423">                                ! The background Laplacian horizontal viscosity.</span>
<span id="L1424">KH_BG_MIN = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1425">                                ! The minimum value allowed for Laplacian horizontal viscosity, KH.</span>
<span id="L1426">KH_VEL_SCALE = 0.01             !   [m s-1] default = 0.0</span>
<span id="L1427">                                ! The velocity scale which is multiplied by the grid spacing to calculate the</span>
<span id="L1428">                                ! Laplacian viscosity. The final viscosity is the largest of this scaled</span>
<span id="L1429">                                ! viscosity, the Smagorinsky and Leith viscosities, and KH.</span>
<span id="L1430">KH_SIN_LAT = 2000.0             !   [m2 s-1] default = 0.0</span>
<span id="L1431">                                ! The amplitude of a latitudinally-dependent background viscosity of the form</span>
<span id="L1432">                                ! KH_SIN_LAT*(SIN(LAT)**KH_PWR_OF_SINE).</span>
<span id="L1433">KH_PWR_OF_SINE = 4.0            !   [nondim] default = 4.0</span>
<span id="L1434">                                ! The power used to raise SIN(LAT) when using a latitudinally dependent</span>
<span id="L1435">                                ! background viscosity.</span>
<span id="L1436">SMAGORINSKY_KH = False          !   [Boolean] default = False</span>
<span id="L1437">                                ! If true, use a Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1438">LEITH_KH = False                !   [Boolean] default = False</span>
<span id="L1439">                                ! If true, use a Leith nonlinear eddy viscosity.</span>
<span id="L1440">RES_SCALE_MEKE_VISC = False     !   [Boolean] default = False</span>
<span id="L1441">                                ! If true, the viscosity contribution from MEKE is scaled by the resolution</span>
<span id="L1442">                                ! function.</span>
<span id="L1443">BOUND_KH = True                 !   [Boolean] default = True</span>
<span id="L1444">                                ! If true, the Laplacian coefficient is locally limited to be stable.</span>
<span id="L1445">EY24_EBT_BS = False             !   [Boolean] default = False</span>
<span id="L1446">                                ! If true, use the the backscatter scheme (EBT mode with kill switch)developed</span>
<span id="L1447">                                ! by Yankovsky et al. (2024).</span>
<span id="L1448">ANISOTROPIC_VISCOSITY = False   !   [Boolean] default = False</span>
<span id="L1449">                                ! If true, allow anistropic viscosity in the Laplacian horizontal viscosity.</span>
<span id="L1450">ADD_LES_VISCOSITY = False       !   [Boolean] default = False</span>
<span id="L1451">                                ! If true, adds the viscosity from Smagorinsky and Leith to the background</span>
<span id="L1452">                                ! viscosity instead of taking the maximum.</span>
<span id="L1453">BIHARMONIC = True               !   [Boolean] default = True</span>
<span id="L1454">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1455">                                ! LAPLACIAN.</span>
<span id="L1456">AH = 0.0                        !   [m4 s-1] default = 0.0</span>
<span id="L1457">                                ! The background biharmonic horizontal viscosity.</span>
<span id="L1458">AH_VEL_SCALE = 0.01             !   [m s-1] default = 0.0</span>
<span id="L1459">                                ! The velocity scale which is multiplied by the cube of the grid spacing to</span>
<span id="L1460">                                ! calculate the biharmonic viscosity. The final viscosity is the largest of this</span>
<span id="L1461">                                ! scaled viscosity, the Smagorinsky and Leith viscosities, and AH.</span>
<span id="L1462">AH_TIME_SCALE = 0.0             !   [s] default = 0.0</span>
<span id="L1463">                                ! A time scale whose inverse is multiplied by the fourth power of the grid</span>
<span id="L1464">                                ! spacing to calculate biharmonic viscosity. The final viscosity is the largest</span>
<span id="L1465">                                ! of all viscosity formulations in use. 0.0 means that it&#x27;s not used.</span>
<span id="L1466">SMAGORINSKY_AH = True           !   [Boolean] default = False</span>
<span id="L1467">                                ! If true, use a biharmonic Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1468">LEITH_AH = False                !   [Boolean] default = False</span>
<span id="L1469">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity.</span>
<span id="L1470">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1471">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1472">                                ! harmonic backscatter.</span>
<span id="L1473">BOUND_AH = True                 !   [Boolean] default = True</span>
<span id="L1474">                                ! If true, the biharmonic coefficient is locally limited to be stable.</span>
<span id="L1475">RE_AH = 0.0                     !   [nondim] default = 0.0</span>
<span id="L1476">                                ! If nonzero, the biharmonic coefficient is scaled so that the biharmonic</span>
<span id="L1477">                                ! Reynolds number is equal to this.</span>
<span id="L1478">BACKSCATTER_UNDERBOUND = False  !   [Boolean] default = False</span>
<span id="L1479">                                ! If true, the bounds on the biharmonic viscosity are allowed to increase where</span>
<span id="L1480">                                ! the Laplacian viscosity is negative (due to backscatter parameterizations)</span>
<span id="L1481">                                ! beyond the largest timestep-dependent stable values of biharmonic viscosity</span>
<span id="L1482">                                ! when no Laplacian viscosity is applied.  The default is true for historical</span>
<span id="L1483">                                ! reasons, but this option probably should not be used because it can contribute</span>
<span id="L1484">                                ! to numerical instabilities.</span>
<span id="L1485">SMAG_BI_CONST = 0.06            !   [nondim] default = 0.0</span>
<span id="L1486">                                ! The nondimensional biharmonic Smagorinsky constant, typically 0.015 - 0.06.</span>
<span id="L1487">BOUND_CORIOLIS_BIHARM = True    !   [Boolean] default = True</span>
<span id="L1488">                                ! If true use a viscosity that increases with the square of the velocity shears,</span>
<span id="L1489">                                ! so that the resulting viscous drag is of comparable magnitude to the Coriolis</span>
<span id="L1490">                                ! terms when the velocity differences between adjacent grid points is</span>
<span id="L1491">                                ! 0.5*BOUND_CORIOLIS_VEL.  The default is the value of BOUND_CORIOLIS (or</span>
<span id="L1492">                                ! false).</span>
<span id="L1493">BOUND_CORIOLIS_VEL = 6.0        !   [m s-1] default = 6.0</span>
<span id="L1494">                                ! The velocity scale at which BOUND_CORIOLIS_BIHARM causes the biharmonic drag</span>
<span id="L1495">                                ! to have comparable magnitude to the Coriolis acceleration.  The default is set</span>
<span id="L1496">                                ! by MAXVEL.</span>
<span id="L1497">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1498">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1499">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1500">                                ! outside of the domain.</span>
<span id="L1501">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L1502">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L1503">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L1504">USE_KH_BG_2D = False            !   [Boolean] default = False</span>
<span id="L1505">                                ! If true, read a file containing 2-d background harmonic viscosities. The final</span>
<span id="L1506">                                ! viscosity is the maximum of the other terms and this background value.</span>
<span id="L1507">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1508">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1509">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1510">                                ! recommended.</span>
<span id="L1511"></span>
<span id="L1512">! === module MOM_vert_friction ===</span>
<span id="L1513">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1514">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1515">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1516">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1517">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1518">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1519">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1520">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1521">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1522">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1523">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1524">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1525">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1526">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1527">                                ! of the ocean in a column.</span>
<span id="L1528">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1529">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1530">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1531">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1532">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1533">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1534">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1535">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1536">HARMONIC_VISC = False           !   [Boolean] default = False</span>
<span id="L1537">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1538">                                ! viscosity.</span>
<span id="L1539">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1540">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1541">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1542">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1543">HMIX_FIXED = 0.5                !   [m]</span>
<span id="L1544">                                ! The prescribed depth over which the near-surface viscosity and diffusivity are</span>
<span id="L1545">                                ! elevated when the bulk mixed layer is not used.</span>
<span id="L1546">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1547">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1548">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1549">KV_ML_INVZ2 = 0.0               !   [m2 s-1] default = 0.0</span>
<span id="L1550">                                ! An extra kinematic viscosity in a mixed layer of thickness HMIX_FIXED, with</span>
<span id="L1551">                                ! the actual viscosity scaling as 1/(z*HMIX_FIXED)^2, where z is the distance</span>
<span id="L1552">                                ! from the surface, to allow for finite wind stresses to be transmitted through</span>
<span id="L1553">                                ! infinitesimally thin surface layers.  This is an older option for numerical</span>
<span id="L1554">                                ! convenience without a strong physical basis, and its use is now discouraged.</span>
<span id="L1555">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1556">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1557">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1558">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1559">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1560">                                ! default is CFL_TRUNCATE.</span>
<span id="L1561">CFL_TRUNCATE_RAMP_TIME = 7200.0 !   [s] default = 0.0</span>
<span id="L1562">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1563">                                ! the run.</span>
<span id="L1564">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1565">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1566">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1567">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1568">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1569">VEL_UNDERFLOW = 0.0             !   [m s-1] default = 0.0</span>
<span id="L1570">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1571">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1572">                                ! divided by the age of the universe.</span>
<span id="L1573"></span>
<span id="L1574">! === module MOM_barotropic ===</span>
<span id="L1575">USE_BT_CONT_TYPE = True         !   [Boolean] default = True</span>
<span id="L1576">                                ! If true, use a structure with elements that describe effective face areas from</span>
<span id="L1577">                                ! the summed continuity solver as a function the barotropic flow in coupling</span>
<span id="L1578">                                ! between the barotropic and baroclinic flow.  This is only used if SPLIT is</span>
<span id="L1579">                                ! true.</span>
<span id="L1580">INTEGRAL_BT_CONTINUITY = False  !   [Boolean] default = False</span>
<span id="L1581">                                ! If true, use the time-integrated velocity over the barotropic steps to</span>
<span id="L1582">                                ! determine the integrated transports used to update the continuity equation.</span>
<span id="L1583">                                ! Otherwise the transports are the sum of the transports based on a series of</span>
<span id="L1584">                                ! instantaneous velocities and the BT_CONT_TYPE for transports.  This is only</span>
<span id="L1585">                                ! valid if USE_BT_CONT_TYPE = True.</span>
<span id="L1586">BOUND_BT_CORRECTION = True      !   [Boolean] default = False</span>
<span id="L1587">                                ! If true, the corrective pseudo mass-fluxes into the barotropic solver are</span>
<span id="L1588">                                ! limited to values that require less than maxCFL_BT_cont to be accommodated.</span>
<span id="L1589">BT_CONT_CORR_BOUNDS = True      !   [Boolean] default = True</span>
<span id="L1590">                                ! If true, and BOUND_BT_CORRECTION is true, use the BT_cont_type variables to</span>
<span id="L1591">                                ! set limits determined by MAXCFL_BT_CONT on the CFL number of the velocities</span>
<span id="L1592">                                ! that are likely to be driven by the corrective mass fluxes.</span>
<span id="L1593">ADJUST_BT_CONT = False          !   [Boolean] default = False</span>
<span id="L1594">                                ! If true, adjust the curve fit to the BT_cont type that is used by the</span>
<span id="L1595">                                ! barotropic solver to match the transport about which the flow is being</span>
<span id="L1596">                                ! linearized.</span>
<span id="L1597">GRADUAL_BT_ICS = False          !   [Boolean] default = False</span>
<span id="L1598">                                ! If true, adjust the initial conditions for the barotropic solver to the values</span>
<span id="L1599">                                ! from the layered solution over a whole timestep instead of instantly. This is</span>
<span id="L1600">                                ! a decent approximation to the inclusion of sum(u dh_dt) while also correcting</span>
<span id="L1601">                                ! for truncation errors.</span>
<span id="L1602">BT_USE_VISC_REM_U_UH0 = False   !   [Boolean] default = False</span>
<span id="L1603">                                ! If true, use the viscous remnants when estimating the barotropic velocities</span>
<span id="L1604">                                ! that were used to calculate uh0 and vh0.  False is probably the better choice.</span>
<span id="L1605">BT_PROJECT_VELOCITY = True      !   [Boolean] default = False</span>
<span id="L1606">                                ! If true, step the barotropic velocity first and project out the velocity</span>
<span id="L1607">                                ! tendency by 1+BEBT when calculating the transport.  The default (false) is to</span>
<span id="L1608">                                ! use a predictor continuity step to find the pressure field, and then to do a</span>
<span id="L1609">                                ! corrector continuity step using a weighted average of the old and new</span>
<span id="L1610">                                ! velocities, with weights of (1-BEBT) and BEBT.</span>
<span id="L1611">BT_NONLIN_STRESS = False        !   [Boolean] default = False</span>
<span id="L1612">                                ! If true, use the full depth of the ocean at the start of the barotropic step</span>
<span id="L1613">                                ! when calculating the surface stress contribution to the barotropic</span>
<span id="L1614">                                ! acclerations.  Otherwise use the depth based on bathyT.</span>
<span id="L1615">DYNAMIC_SURFACE_PRESSURE = True !   [Boolean] default = False</span>
<span id="L1616">                                ! If true, add a dynamic pressure due to a viscous ice shelf, for instance.</span>
<span id="L1617">ICE_LENGTH_DYN_PSURF = 1.0E+04  !   [m] default = 1.0E+04</span>
<span id="L1618">                                ! The length scale at which the Rayleigh damping rate due to the ice strength</span>
<span id="L1619">                                ! should be the same as if a Laplacian were applied, if DYNAMIC_SURFACE_PRESSURE</span>
<span id="L1620">                                ! is true.</span>
<span id="L1621">DEPTH_MIN_DYN_PSURF = 1.0E-06   !   [m] default = 1.0E-06</span>
<span id="L1622">                                ! The minimum depth to use in limiting the size of the dynamic surface pressure</span>
<span id="L1623">                                ! for stability, if DYNAMIC_SURFACE_PRESSURE is true..</span>
<span id="L1624">CONST_DYN_PSURF = 0.9           !   [nondim] default = 0.9</span>
<span id="L1625">                                ! The constant that scales the dynamic surface pressure, if</span>
<span id="L1626">                                ! DYNAMIC_SURFACE_PRESSURE is true.  Stable values are &lt; ~1.0.</span>
<span id="L1627">BT_CORIOLIS_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1628">                                ! A factor by which the barotropic Coriolis anomaly terms are scaled.</span>
<span id="L1629">BAROTROPIC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1630">                                ! The vintage of the expressions in the barotropic solver. Values below 20190101</span>
<span id="L1631">                                ! recover the answers from the end of 2018, while higher values use more</span>
<span id="L1632">                                ! efficient or general expressions.</span>
<span id="L1633">VISC_REM_BT_WEIGHT_BUG = False  !   [Boolean] default = False</span>
<span id="L1634">                                ! If true, recover a bug in barotropic solver that uses an unnormalized weight</span>
<span id="L1635">                                ! function for vertical averages of baroclinic velocity and forcing. Default of</span>
<span id="L1636">                                ! this flag is set by VISC_REM_BUG.</span>
<span id="L1637">TIDAL_SAL_FLATHER = False       !   [Boolean] default = False</span>
<span id="L1638">                                ! If true, then apply adjustments to the external gravity wave speed used with</span>
<span id="L1639">                                ! the Flather OBC routine consistent with the barotropic solver. This applies to</span>
<span id="L1640">                                ! cases with  tidal forcing using the scalar self-attraction approximation. The</span>
<span id="L1641">                                ! default is currently False in order to retain previous answers but should be</span>
<span id="L1642">                                ! set to True for new experiments</span>
<span id="L1643">SADOURNY = True                 !   [Boolean] default = True</span>
<span id="L1644">                                ! If true, the Coriolis terms are discretized with the Sadourny (1975) energy</span>
<span id="L1645">                                ! conserving scheme, otherwise the Arakawa &amp; Hsu scheme is used.  If the</span>
<span id="L1646">                                ! internal deformation radius is not resolved, the Sadourny scheme should</span>
<span id="L1647">                                ! probably be used.</span>
<span id="L1648">BT_THICK_SCHEME = &quot;FROM_BT_CONT&quot; ! default = &quot;FROM_BT_CONT&quot;</span>
<span id="L1649">                                ! A string describing the scheme that is used to set the open face areas used</span>
<span id="L1650">                                ! for barotropic transport and the relative weights of the accelerations. Valid</span>
<span id="L1651">                                ! values are:</span>
<span id="L1652">                                !    ARITHMETIC - arithmetic mean layer thicknesses</span>
<span id="L1653">                                !    HARMONIC - harmonic mean layer thicknesses</span>
<span id="L1654">                                !    HYBRID (the default) - use arithmetic means for</span>
<span id="L1655">                                !       layers above the shallowest bottom, the harmonic</span>
<span id="L1656">                                !       mean for layers below, and a weighted average for</span>
<span id="L1657">                                !       layers that straddle that depth</span>
<span id="L1658">                                !    FROM_BT_CONT - use the average thicknesses kept</span>
<span id="L1659">                                !       in the h_u and h_v fields of the BT_cont_type</span>
<span id="L1660">BT_STRONG_DRAG = False          !   [Boolean] default = False</span>
<span id="L1661">                                ! If true, use a stronger estimate of the retarding effects of strong bottom</span>
<span id="L1662">                                ! drag, by making it implicit with the barotropic time-step instead of implicit</span>
<span id="L1663">                                ! with the baroclinic time-step and dividing by the number of barotropic steps.</span>
<span id="L1664">BT_LINEAR_WAVE_DRAG = False     !   [Boolean] default = False</span>
<span id="L1665">                                ! If true, apply a linear drag to the barotropic velocities, using rates set by</span>
<span id="L1666">                                ! lin_drag_u &amp; _v divided by the depth of the ocean.  This was introduced to</span>
<span id="L1667">                                ! facilitate tide modeling.</span>
<span id="L1668">BT_LINEAR_FREQ_DRAG = False     !   [Boolean] default = False</span>
<span id="L1669">                                ! If true, apply frequency-dependent drag to the tidal velocities. The streaming</span>
<span id="L1670">                                ! band-pass filter must be turned on.</span>
<span id="L1671">CLIP_BT_VELOCITY = False        !   [Boolean] default = False</span>
<span id="L1672">                                ! If true, limit any velocity components that exceed CFL_TRUNCATE.  This should</span>
<span id="L1673">                                ! only be used as a desperate debugging measure.</span>
<span id="L1674">MAXCFL_BT_CONT = 0.25           !   [nondim] default = 0.25</span>
<span id="L1675">                                ! The maximum permitted CFL number associated with the barotropic accelerations</span>
<span id="L1676">                                ! from the summed velocities times the time-derivatives of thicknesses.</span>
<span id="L1677">DT_BT_FILTER = -0.25            !   [sec or nondim] default = -0.25</span>
<span id="L1678">                                ! A time-scale over which the barotropic mode solutions are filtered, in seconds</span>
<span id="L1679">                                ! if positive, or as a fraction of DT if negative. When used this can never be</span>
<span id="L1680">                                ! taken to be longer than 2*dt.  Set this to 0 to apply no filtering.</span>
<span id="L1681">G_BT_EXTRA = 0.0                !   [nondim] default = 0.0</span>
<span id="L1682">                                ! A nondimensional factor by which gtot is enhanced.</span>
<span id="L1683">SSH_EXTRA = 10.0                !   [m] default = 10.0</span>
<span id="L1684">                                ! An estimate of how much higher SSH might get, for use in calculating the safe</span>
<span id="L1685">                                ! external wave speed. The default is the minimum of 10 m or 5% of</span>
<span id="L1686">                                ! MAXIMUM_DEPTH.</span>
<span id="L1687">LINEARIZED_BT_CORIOLIS = True   !   [Boolean] default = True</span>
<span id="L1688">                                ! If true use the bottom depth instead of the total water column thickness in</span>
<span id="L1689">                                ! the barotropic Coriolis term calculations.</span>
<span id="L1690">BEBT = 0.2                      !   [nondim] default = 0.1</span>
<span id="L1691">                                ! BEBT determines whether the barotropic time stepping uses the forward-backward</span>
<span id="L1692">                                ! time-stepping scheme or a backward Euler scheme. BEBT is valid in the range</span>
<span id="L1693">                                ! from 0 (for a forward-backward treatment of nonrotating gravity waves) to 1</span>
<span id="L1694">                                ! (for a backward Euler treatment). In practice, BEBT must be greater than about</span>
<span id="L1695">                                ! 0.05.</span>
<span id="L1696">DTBT = -0.9                     !   [s or nondim] default = -0.98</span>
<span id="L1697">                                ! The barotropic time step, in s. DTBT is only used with the split explicit time</span>
<span id="L1698">                                ! stepping. To set the time step automatically based the maximum stable value</span>
<span id="L1699">                                ! use 0, or a negative value gives the fraction of the stable value. Setting</span>
<span id="L1700">                                ! DTBT to 0 is the same as setting it to -0.98. The value of DTBT that will</span>
<span id="L1701">                                ! actually be used is an integer fraction of DT, rounding down.</span>
<span id="L1702">BT_USE_OLD_CORIOLIS_BRACKET_BUG = False !   [Boolean] default = False</span>
<span id="L1703">                                ! If True, use an order of operations that is not bitwise rotationally symmetric</span>
<span id="L1704">                                ! in the meridional Coriolis term of the barotropic solver.</span>
<span id="L1705">MASK_COASTAL_PRESSURE_FORCE = False !   [Boolean] default = False</span>
<span id="L1706">                                ! If true, use the land masks to zero out the diagnosed barotropic pressure</span>
<span id="L1707">                                ! gradient accelerations at coastal or land points.  This changes diagnostics</span>
<span id="L1708">                                ! and improves the reproducibility of certain debugging checksums, but it does</span>
<span id="L1709">                                ! not alter the solutions themselves.</span>
<span id="L1710"></span>
<span id="L1711">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1712">MIXEDLAYER_RESTRAT = True       !   [Boolean] default = False</span>
<span id="L1713">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1714">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1715">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1716">MLE%</span>
<span id="L1717">USE_BODNER23 = True             !   [Boolean] default = False</span>
<span id="L1718">                                ! If true, use the Bodner et al., 2023, formulation of the re-stratifying</span>
<span id="L1719">                                ! mixed-layer restratification parameterization. This only works in ALE mode.</span>
<span id="L1720">CR = 0.0175                     !   [nondim] default = 0.0</span>
<span id="L1721">                                ! The efficiency coefficient in eq 27 of Bodner et al., 2023.</span>
<span id="L1722">BODNER_NSTAR = 0.066            !   [nondim] default = 0.066</span>
<span id="L1723">                                ! The n* value used to estimate the turbulent vertical momentum flux in Bodner</span>
<span id="L1724">                                ! et al., 2023, eq. 18. This is independent of the value used in the PBL scheme</span>
<span id="L1725">                                ! but should be set to be the same for consistency.</span>
<span id="L1726">BODNER_MSTAR = 0.5              !   [nondim] default = 0.5</span>
<span id="L1727">                                ! The m* value used to estimate the turbulent vertical momentum flux in Bodner</span>
<span id="L1728">                                ! et al., 2023, eq. 18. This is independent of the value used in the PBL scheme</span>
<span id="L1729">                                ! but should be set to be the same for consistency.</span>
<span id="L1730">BLD_GROWING_TFILTER = 0.0       !   [s] default = 0.0</span>
<span id="L1731">                                ! The time-scale for a running-mean filter applied to the boundary layer depth</span>
<span id="L1732">                                ! (BLD) when the BLD is deeper than the running mean. A value of 0</span>
<span id="L1733">                                ! instantaneously sets the running mean to the current value of BLD.</span>
<span id="L1734">BLD_DECAYING_TFILTER = 8.64E+04 !   [s] default = 0.0</span>
<span id="L1735">                                ! The time-scale for a running-mean filter applied to the boundary layer depth</span>
<span id="L1736">                                ! (BLD) when the BLD is shallower than the running mean. A value of 0</span>
<span id="L1737">                                ! instantaneously sets the running mean to the current value of BLD.</span>
<span id="L1738">MLD_GROWING_TFILTER = 0.0       !   [s] default = 0.0</span>
<span id="L1739">                                ! The time-scale for a running-mean filter applied to the time-filtered BLD,</span>
<span id="L1740">                                ! when the latter is deeper than the running mean. A value of 0 instantaneously</span>
<span id="L1741">                                ! sets the running mean to the current value filtered BLD.</span>
<span id="L1742">MLD_DECAYING_TFILTER = 2.592E+06 !   [s] default = 0.0</span>
<span id="L1743">                                ! The time-scale for a running-mean filter applied to the time-filtered BLD,</span>
<span id="L1744">                                ! when the latter is shallower than the running mean. A value of 0</span>
<span id="L1745">                                ! instantaneously sets the running mean to the current value filtered BLD.</span>
<span id="L1746">ML_RESTRAT_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1747">                                ! The vintage of the order of arithmetic and expressions in the mixed layer</span>
<span id="L1748">                                ! restrat calculations.  Values below 20240201 recover the answers from the end</span>
<span id="L1749">                                ! of 2023, while higher values use the new cuberoot function in the Bodner code</span>
<span id="L1750">                                ! to avoid needing to undo dimensional rescaling.</span>
<span id="L1751">BODNER_HMIN_BUG = True          !   [Boolean] default = True</span>
<span id="L1752">                                ! If true, recover a bug where layer thicknesses in the Bodner et al. mixed</span>
<span id="L1753">                                ! layer restratification are not clamped at a minimum value and can therefore go</span>
<span id="L1754">                                ! negative.</span>
<span id="L1755">MIN_WSTAR2 = 1.0E-09            !   [m2 s-2] default = 1.0E-24</span>
<span id="L1756">                                ! The minimum lower bound to apply to the vertical momentum flux, w&#x27;u&#x27;, in the</span>
<span id="L1757">                                ! Bodner et al., restratification parameterization. This avoids a</span>
<span id="L1758">                                ! division-by-zero in the limit when u* and the buoyancy flux are zero.  The</span>
<span id="L1759">                                ! default is less than the molecular viscosity of water times the Coriolis</span>
<span id="L1760">                                ! parameter a micron away from the equator.</span>
<span id="L1761">TAIL_DH = 0.0                   !   [nondim] default = 0.0</span>
<span id="L1762">                                ! Fraction by which to extend the mixed-layer restratification depth used for a</span>
<span id="L1763">                                ! smoother stream function at the base of the mixed-layer.</span>
<span id="L1764">USE_STANLEY_TVAR = False        !   [Boolean] default = False</span>
<span id="L1765">                                ! If true, turn on Stanley SGS T variance parameterization in ML restrat code.</span>
<span id="L1766">USE_CR_GRID = False             !   [Boolean] default = False</span>
<span id="L1767">                                ! If true, read in a spatially varying Cr field.</span>
<span id="L1768">USE_MLD_GRID = False            !   [Boolean] default = False</span>
<span id="L1769">                                ! If true, read in a spatially varying MLD_decaying_Tfilt field.</span>
<span id="L1770">%MLE</span>
<span id="L1771">MLE_USE_PBL_MLD = True          !   [Boolean] default = False</span>
<span id="L1772">                                ! If true, the MLE parameterization will use the mixed-layer depth provided by</span>
<span id="L1773">                                ! the active PBL parameterization. If false, MLE will estimate a MLD based on a</span>
<span id="L1774">                                ! density difference with the surface using the parameter MLE_DENSITY_DIFF,</span>
<span id="L1775">                                ! unless BODNER_DETECT_MLD is true.</span>
<span id="L1776">BODNER_DETECT_MLD = False       !   [Boolean] default = False</span>
<span id="L1777">                                ! If true, the Bodner parameterization will use the mixed-layer depth detected</span>
<span id="L1778">                                ! via the density difference criterion MLE_DENSITY_DIFF.</span>
<span id="L1779"></span>
<span id="L1780">! === module MOM_diagnostics ===</span>
<span id="L1781">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1782">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1783">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1784">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1785">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1786">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1787">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = False !   [Boolean] default = False</span>
<span id="L1788">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1789">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1790">                                ! this option to false.</span>
<span id="L1791"></span>
<span id="L1792">! === module MOM_diabatic_driver ===</span>
<span id="L1793">! The following parameters are used for diabatic processes.</span>
<span id="L1794">USE_LEGACY_DIABATIC_DRIVER = False !   [Boolean] default = True</span>
<span id="L1795">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1796">                                ! and is needed to avoid change in answers.</span>
<span id="L1797">ENERGETICS_SFC_PBL = True       !   [Boolean] default = False</span>
<span id="L1798">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1799">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1800">EPBL_IS_ADDITIVE = False        !   [Boolean] default = True</span>
<span id="L1801">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1802">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1803">PRANDTL_EPBL = 1.0              !   [nondim] default = 1.0</span>
<span id="L1804">                                ! The Prandtl number used by ePBL to convert vertical diffusivities into</span>
<span id="L1805">                                ! viscosities.</span>
<span id="L1806">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1807">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1808">                                ! internal tide energy density.</span>
<span id="L1809">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1810">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1811">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1812">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1813">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1814">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1815">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1816">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1817">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1818">                                ! updated state.</span>
<span id="L1819">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1820">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1821">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1822">MIX_BOUNDARY_TRACER_ALE = False !   [Boolean] default = False</span>
<span id="L1823">                                ! If true and in ALE mode, mix the passive tracers in massless layers at the</span>
<span id="L1824">                                ! bottom into the interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1825">KD_MIN_TR = 1.5E-06             !   [m2 s-1] default = 1.5E-06</span>
<span id="L1826">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1827">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1828">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1829">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1830">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1831">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1832">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1833">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1834">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1835">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1836">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1837">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1838">                                ! scale.</span>
<span id="L1839">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1840">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1841">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1842">                                ! through the column.</span>
<span id="L1843">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1844">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1845">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1846">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1847">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1848">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1849">HREF_FOR_MLD = 0.0              !   [m] default = 0.0</span>
<span id="L1850">                                ! Reference depth used to calculate the potential density used to find the mixed</span>
<span id="L1851">                                ! layer depth based on a delta rho = 0.03 kg/m3.</span>
<span id="L1852">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1853">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1854">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1855">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1856">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1857">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1858">                                ! base of the mixed layer.</span>
<span id="L1859"></span>
<span id="L1860">! === module MOM_CVMix_KPP ===</span>
<span id="L1861">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1862">! See http://cvmix.github.io/</span>
<span id="L1863">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1864">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1865">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1866"></span>
<span id="L1867">! === module MOM_CVMix_conv ===</span>
<span id="L1868">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1869">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1870">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1871">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1872">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1873"></span>
<span id="L1874">! === module MOM_set_diffusivity ===</span>
<span id="L1875">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1876">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1877">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1878">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1879">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1880">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1881">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1882">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1883">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1884">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1885"></span>
<span id="L1886">! === module MOM_tidal_mixing ===</span>
<span id="L1887">! Vertical Tidal Mixing Parameterization</span>
<span id="L1888">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1889">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1890">INT_TIDE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L1891">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1892">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1893">ML_RADIATION = False            !   [Boolean] default = False</span>
<span id="L1894">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L1895">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L1896">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L1897">BBL_EFFIC = 0.01                !   [nondim] default = 0.2</span>
<span id="L1898">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L1899">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1900">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L1901">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L1902">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L1903">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L1904">BBL_MIXING_AS_MAX = False       !   [Boolean] default = True</span>
<span id="L1905">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L1906">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L1907">USE_LOTW_BBL_DIFFUSIVITY = True !   [Boolean] default = False</span>
<span id="L1908">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L1909">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L1910">                                ! scheme.</span>
<span id="L1911">LOTW_BBL_USE_OMEGA = True       !   [Boolean] default = True</span>
<span id="L1912">                                ! If true, use the maximum of Omega and N for the TKE to diffusion calculation.</span>
<span id="L1913">                                ! Otherwise, N is N.</span>
<span id="L1914">VON_KARMAN_BBL = 0.41           !   [nondim] default = 0.41</span>
<span id="L1915">                                ! The value the von Karman constant as used in calculating the BBL diffusivity.</span>
<span id="L1916">LOTW_BBL_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1917">                                ! The vintage of the order of arithmetic and expressions in the LOTW_BBL</span>
<span id="L1918">                                ! calculations.  Values below 20240630 recover the original answers, while</span>
<span id="L1919">                                ! higher values use more accurate expressions.  This only applies when</span>
<span id="L1920">                                ! USE_LOTW_BBL_DIFFUSIVITY is true.</span>
<span id="L1921">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L1922">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L1923">                                ! boundary layer density.</span>
<span id="L1924"></span>
<span id="L1925">! === module MOM_bkgnd_mixing ===</span>
<span id="L1926">! Adding static vertical background mixing coefficients</span>
<span id="L1927">KD = 1.5E-05                    !   [m2 s-1] default = 0.0</span>
<span id="L1928">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L1929">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L1930">KD_MIN = 2.0E-06                !   [m2 s-1] default = 1.5E-07</span>
<span id="L1931">                                ! The minimum diapycnal diffusivity.</span>
<span id="L1932">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1933">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L1934">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L1935">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L1936">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L1937">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L1938">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L1939">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L1940">                                ! into viscosities.</span>
<span id="L1941">HENYEY_IGW_BACKGROUND = True    !   [Boolean] default = False</span>
<span id="L1942">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L1943">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L1944">HENYEY_N0_2OMEGA = 20.0         !   [nondim] default = 20.0</span>
<span id="L1945">                                ! The ratio of the typical Buoyancy frequency to twice the Earth&#x27;s rotation</span>
<span id="L1946">                                ! period, used with the Henyey scaling from the mixing.</span>
<span id="L1947">HENYEY_MAX_LAT = 73.0           !   [degN] default = 95.0</span>
<span id="L1948">                                ! A latitude poleward of which the Henyey profile is returned to the minimum</span>
<span id="L1949">                                ! diffusivity</span>
<span id="L1950">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L1951">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L1952">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L1953">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L1954">KD_MAX = 0.1                    !   [m2 s-1] default = -1.0</span>
<span id="L1955">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L1956">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L1957">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1958">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L1959">                                ! or scaling.</span>
<span id="L1960">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L1961">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L1962">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L1963">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L1964">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L1965">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L1966">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L1967">                                ! = A + B*N.</span>
<span id="L1968">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L1969">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L1970">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L1971">                                ! = A + B*N</span>
<span id="L1972">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L1973">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L1974">DOUBLE_DIFFUSION = True         !   [Boolean] default = False</span>
<span id="L1975">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L1976">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L1977">MAX_RRHO_SALT_FINGERS = 2.55    !   [nondim] default = 1.9</span>
<span id="L1978">                                ! Maximum density ratio for salt fingering regime.</span>
<span id="L1979">MAX_SALT_DIFF_SALT_FINGERS = 1.0E-04 !   [m2 s-1] default = 1.0E-04</span>
<span id="L1980">                                ! Maximum salt diffusivity for salt fingering regime.</span>
<span id="L1981">KV_MOLECULAR = 1.5E-06          !   [m2 s-1] default = 1.5E-06</span>
<span id="L1982">                                ! Molecular viscosity for calculation of fluxes under double-diffusive</span>
<span id="L1983">                                ! convection.</span>
<span id="L1984"></span>
<span id="L1985">! === module MOM_kappa_shear ===</span>
<span id="L1986">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L1987">USE_JACKSON_PARAM = True        !   [Boolean] default = False</span>
<span id="L1988">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L1989">                                ! parameterization.</span>
<span id="L1990">VERTEX_SHEAR = True             !   [Boolean] default = False</span>
<span id="L1991">                                ! If true, do the calculations of the shear-driven mixing at the cell vertices</span>
<span id="L1992">                                ! (i.e., the vorticity points).</span>
<span id="L1993">VERTEX_SHEAR_VISCOSITY_BUG = True !   [Boolean] default = True</span>
<span id="L1994">                                ! If true, use a bug in vertex shear that zeros out viscosities at vertices on</span>
<span id="L1995">                                ! coastlines.</span>
<span id="L1996">VERTEX_SHEAR_GEOMETRIC_MEAN = False !   [Boolean] default = False</span>
<span id="L1997">                                ! If true, use a geometric mean for moving diffusivity from vertices to tracer</span>
<span id="L1998">                                ! points.  False uses algebraic mean.</span>
<span id="L1999">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L2000">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L2001">                                ! tracer points in the kappa shear solver.</span>
<span id="L2002">RINO_CRIT = 0.25                !   [nondim] default = 0.25</span>
<span id="L2003">                                ! The critical Richardson number for shear mixing.</span>
<span id="L2004">SHEARMIX_RATE = 0.089           !   [nondim] default = 0.089</span>
<span id="L2005">                                ! A nondimensional rate scale for shear-driven entrainment. Jackson et al find</span>
<span id="L2006">                                ! values in the range of 0.085-0.089.</span>
<span id="L2007">MAX_RINO_IT = 25                !   [nondim] default = 50</span>
<span id="L2008">                                ! The maximum number of iterations that may be used to estimate the Richardson</span>
<span id="L2009">                                ! number driven mixing.</span>
<span id="L2010">KD_KAPPA_SHEAR_0 = 1.5E-05      !   [m2 s-1] default = 1.5E-05</span>
<span id="L2011">                                ! The background diffusivity that is used to smooth the density and shear</span>
<span id="L2012">                                ! profiles before solving for the diffusivities.  The default is the greater of</span>
<span id="L2013">                                ! KD and 1e-7 m2 s-1.</span>
<span id="L2014">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L2015">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L2016">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L2017">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L2018">KD_TRUNC_KAPPA_SHEAR = 1.5E-07  !   [m2 s-1] default = 1.5E-07</span>
<span id="L2019">                                ! The value of shear-driven diffusivity that is considered negligible and is</span>
<span id="L2020">                                ! rounded down to 0. The default is 1% of KD_KAPPA_SHEAR_0.</span>
<span id="L2021">FRI_CURVATURE = -0.97           !   [nondim] default = -0.97</span>
<span id="L2022">                                ! The nondimensional curvature of the function of the Richardson number in the</span>
<span id="L2023">                                ! kappa source term in the Jackson et al. scheme.</span>
<span id="L2024">TKE_N_DECAY_CONST = 0.24        !   [nondim] default = 0.24</span>
<span id="L2025">                                ! The coefficient for the decay of TKE due to stratification (i.e. proportional</span>
<span id="L2026">                                ! to N*tke). The values found by Jackson et al. are 0.24-0.28.</span>
<span id="L2027">TKE_SHEAR_DECAY_CONST = 0.14    !   [nondim] default = 0.14</span>
<span id="L2028">                                ! The coefficient for the decay of TKE due to shear (i.e. proportional to</span>
<span id="L2029">                                ! |S|*tke). The values found by Jackson et al. are 0.14-0.12.</span>
<span id="L2030">KAPPA_BUOY_SCALE_COEF = 0.82    !   [nondim] default = 0.82</span>
<span id="L2031">                                ! The coefficient for the buoyancy length scale in the kappa equation.  The</span>
<span id="L2032">                                ! values found by Jackson et al. are in the range of 0.81-0.86.</span>
<span id="L2033">KAPPA_N_OVER_S_SCALE_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L2034">                                ! The square of the ratio of the coefficients of the buoyancy and shear scales</span>
<span id="L2035">                                ! in the diffusivity equation, Set this to 0 (the default) to eliminate the</span>
<span id="L2036">                                ! shear scale. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L2037">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L2038">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L2039">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L2040">                                ! the growth of shear instabilies [nondim].</span>
<span id="L2041">KAPPA_SHEAR_TOL_ERR = 0.1       !   [nondim] default = 0.1</span>
<span id="L2042">                                ! The fractional error in kappa that is tolerated. Iteration stops when changes</span>
<span id="L2043">                                ! between subsequent iterations are smaller than this everywhere in a column.</span>
<span id="L2044">                                ! The peak diffusivities usually converge most rapidly, and have much smaller</span>
<span id="L2045">                                ! errors than this.</span>
<span id="L2046">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L2047">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L2048">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L2049">KAPPA_SHEAR_ELIM_MASSLESS = True !   [Boolean] default = True</span>
<span id="L2050">                                ! If true, massless layers are merged with neighboring massive layers in this</span>
<span id="L2051">                                ! calculation.  The default is true and I can think of no good reason why it</span>
<span id="L2052">                                ! should be false. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L2053">MAX_KAPPA_SHEAR_IT = 13         ! default = 13</span>
<span id="L2054">                                ! The maximum number of iterations that may be used to estimate the</span>
<span id="L2055">                                ! time-averaged diffusivity.</span>
<span id="L2056">PRANDTL_TURB = 1.0              !   [nondim] default = 1.0</span>
<span id="L2057">                                ! The turbulent Prandtl number applied to shear instability.</span>
<span id="L2058">KAPPA_SHEAR_MAX_KAP_SRC_CHG = 10.0 !   [nondim] default = 10.0</span>
<span id="L2059">                                ! The maximum permitted increase in the kappa source within an iteration</span>
<span id="L2060">                                ! relative to the local source; this must be greater than 1.  The lower limit</span>
<span id="L2061">                                ! for the permitted fractional decrease is (1 - 0.5/kappa_src_max_chg).  These</span>
<span id="L2062">                                ! limits could perhaps be made dynamic with an improved iterative solver.</span>
<span id="L2063">KAPPA_SHEAR_VERTEX_PSURF_BUG = False !   [Boolean] default = False</span>
<span id="L2064">                                ! If true, do a simple average of the cell surface pressures to get a pressure</span>
<span id="L2065">                                ! at the corner if VERTEX_SHEAR=True.  Otherwise mask out any land points in the</span>
<span id="L2066">                                ! average.</span>
<span id="L2067">KAPPA_SHEAR_ITER_BUG = False    !   [Boolean] default = False</span>
<span id="L2068">                                ! If true, use an older, dimensionally inconsistent estimate of the derivative</span>
<span id="L2069">                                ! of diffusivity with energy in the Newton&#x27;s method iteration.  The bug causes</span>
<span id="L2070">                                ! undercorrections when dz &gt; 1 m.</span>
<span id="L2071">KAPPA_SHEAR_ALL_LAYER_TKE_BUG = False !   [Boolean] default = False</span>
<span id="L2072">                                ! If true, report back the latest estimate of TKE instead of the time average</span>
<span id="L2073">                                ! TKE when there is mass in all layers.  Otherwise always report the time</span>
<span id="L2074">                                ! averaged TKE, as is currently done when there are some massless layers.</span>
<span id="L2075">USE_RESTRICTIVE_TOLERANCE_CHECK = True !   [Boolean] default = False</span>
<span id="L2076">                                ! If true, uses the more restrictive tolerance check to determine if a timestep</span>
<span id="L2077">                                ! is acceptable for the KS_it outer iteration loop.  False uses the original</span>
<span id="L2078">                                ! less restrictive check.</span>
<span id="L2079"></span>
<span id="L2080">! === module MOM_CVMix_shear ===</span>
<span id="L2081">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L2082">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L2083">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L2084">                                ! parameterization.</span>
<span id="L2085">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L2086">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L2087">                                ! parameterization.</span>
<span id="L2088"></span>
<span id="L2089">! === module MOM_CVMix_ddiff ===</span>
<span id="L2090">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L2091">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L2092">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L2093">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L2094">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L2095"></span>
<span id="L2096">! === module MOM_diabatic_aux ===</span>
<span id="L2097">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L2098">RECLAIM_FRAZIL = True           !   [Boolean] default = True</span>
<span id="L2099">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L2100">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L2101">                                ! is above the freezing point.</span>
<span id="L2102">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L2103">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L2104">                                ! net surface salt fluxes within a timestep.</span>
<span id="L2105">PRESSURE_DEPENDENT_FRAZIL = True !   [Boolean] default = False</span>
<span id="L2106">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L2107">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L2108">                                ! cavities.</span>
<span id="L2109">IGNORE_FLUXES_OVER_LAND = False !   [Boolean] default = False</span>
<span id="L2110">                                ! If true, the model does not check if fluxes are being applied over land</span>
<span id="L2111">                                ! points. This is needed when the ocean is coupled with ice shelves and sea ice,</span>
<span id="L2112">                                ! since the sea ice mask needs to be different than the ocean mask to avoid sea</span>
<span id="L2113">                                ! ice formation under ice shelves. This flag only works when use_ePBL = True.</span>
<span id="L2114">DO_RIVERMIX = False             !   [Boolean] default = False</span>
<span id="L2115">                                ! If true, apply additional mixing wherever there is runoff, so that it is mixed</span>
<span id="L2116">                                ! down to RIVERMIX_DEPTH if the ocean is that deep.</span>
<span id="L2117">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L2118">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L2119">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L2120">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L2121">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L2122">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L2123">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L2124">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L2125">VAR_PEN_SW = True               !   [Boolean] default = False</span>
<span id="L2126">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L2127">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L2128">CHL_FROM_FILE = True            !   [Boolean] default = True</span>
<span id="L2129">                                ! If true, chl_a is read from a file.</span>
<span id="L2130">CHL_FILE = &quot;chl_globcolour_monthly_clim.nc&quot; !</span>
<span id="L2131">                                ! CHL_FILE is the file containing chl_a concentrations in the variable CHL_A. It</span>
<span id="L2132">                                ! is used when VAR_PEN_SW and CHL_FROM_FILE are true.</span>
<span id="L2133">CHL_VARNAME = &quot;CHL&quot;             ! default = &quot;CHL_A&quot;</span>
<span id="L2134">                                ! Name of CHL_A variable in CHL_FILE.</span>
<span id="L2135"></span>
<span id="L2136">! === module MOM_energetic_PBL ===</span>
<span id="L2137">ML_OMEGA_FRAC = 0.001           !   [nondim] default = 0.0</span>
<span id="L2138">                                ! When setting the decay scale for turbulence, use this fraction of the absolute</span>
<span id="L2139">                                ! rotation rate blended with the local value of f, as sqrt((1-of)*f^2 +</span>
<span id="L2140">                                ! of*4*omega^2).</span>
<span id="L2141">EKMAN_SCALE_COEF = 1.0          !   [nondim] default = 1.0</span>
<span id="L2142">                                ! A nondimensional scaling factor controlling the inhibition of the diffusive</span>
<span id="L2143">                                ! length scale by rotation. Making this larger decreases the PBL diffusivity.</span>
<span id="L2144">EPBL_ANSWER_DATE = 99991231     ! default = 99991231</span>
<span id="L2145">                                ! The vintage of the order of arithmetic and expressions in the energetic PBL</span>
<span id="L2146">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L2147">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L2148">                                ! Values below 20240101 use A**(1./3.) to estimate the cube root of A in several</span>
<span id="L2149">                                ! expressions, while higher values use the integer root function cuberoot(A) and</span>
<span id="L2150">                                ! therefore can work with scaled variables.</span>
<span id="L2151">EPBL_ORIGINAL_PE_CALC = True    !   [Boolean] default = True</span>
<span id="L2152">                                ! If true, the ePBL code uses the original form of the potential energy change</span>
<span id="L2153">                                ! code.  Otherwise, the newer version that can work with successive increments</span>
<span id="L2154">                                ! to the diffusivity in upward or downward passes is used.</span>
<span id="L2155">MKE_TO_TKE_EFFIC = 0.0          !   [nondim] default = 0.0</span>
<span id="L2156">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L2157">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.</span>
<span id="L2158">TKE_DECAY = 0.01                !   [nondim] default = 2.5</span>
<span id="L2159">                                ! TKE_DECAY relates the vertical rate of decay of the TKE available for</span>
<span id="L2160">                                ! mechanical entrainment to the natural Ekman depth.</span>
<span id="L2161">DIRECT_EPBL_MIXING_CALC = False !   [Boolean] default = False</span>
<span id="L2162">                                ! If true and there is no conversion from mean kinetic energy to ePBL turbulent</span>
<span id="L2163">                                ! kinetic energy, use a direct calculation of the diffusivity that is supported</span>
<span id="L2164">                                ! by a given energy input instead of the more general but slower iterative</span>
<span id="L2165">                                ! solver.</span>
<span id="L2166">EPBL_MSTAR_SCHEME = &quot;OM4&quot;       ! default = &quot;CONSTANT&quot;</span>
<span id="L2167">                                ! EPBL_MSTAR_SCHEME selects the method for setting mstar.  Valid values are:</span>
<span id="L2168">                                !    CONSTANT   - Use a fixed mstar given by MSTAR</span>
<span id="L2169">                                !    OM4        - Use L_Ekman/L_Obukhov in the stabilizing limit, as in OM4</span>
<span id="L2170">                                !    REICHL_H18 - Use the scheme documented in Reichl &amp; Hallberg, 2018.</span>
<span id="L2171">MSTAR_CAP = 1.25                !   [nondim] default = -1.0</span>
<span id="L2172">                                ! If this value is positive, it sets the maximum value of mstar allowed in ePBL.</span>
<span id="L2173">                                ! (This is not used if EPBL_mstar_scheme = CONSTANT).</span>
<span id="L2174">MSTAR2_COEF1 = 0.29             !   [nondim] default = 0.3</span>
<span id="L2175">                                ! Coefficient in computing mstar when rotation and stabilizing effects are both</span>
<span id="L2176">                                ! important (used if EPBL_mstar_scheme = OM4).</span>
<span id="L2177">MSTAR2_COEF2 = 0.152            !   [nondim] default = 0.085</span>
<span id="L2178">                                ! Coefficient in computing mstar when only rotation limits the total mixing</span>
<span id="L2179">                                ! (used if EPBL_MSTAR_SCHEME = OM4)</span>
<span id="L2180">EPBL_BBL_USE_MSTAR = False      !   [nondim] default = False</span>
<span id="L2181">                                ! A logical to use mstar in the calculation of TKE in the ePBL BBL scheme</span>
<span id="L2182">NSTAR = 0.06                    !   [nondim] default = 0.2</span>
<span id="L2183">                                ! The portion of the buoyant potential energy imparted by surface fluxes that is</span>
<span id="L2184">                                ! available to drive entrainment at the base of mixed layer when that energy is</span>
<span id="L2185">                                ! positive.</span>
<span id="L2186">MSTAR_CONV_ADJ = 0.667          !   [nondim] default = 0.0</span>
<span id="L2187">                                ! Coefficient used for reducing mstar during convection due to reduction of</span>
<span id="L2188">                                ! stable density gradient.</span>
<span id="L2189">USE_MLD_ITERATION = True        !   [Boolean] default = True</span>
<span id="L2190">                                ! A logical that specifies whether or not to use the distance to the bottom of</span>
<span id="L2191">                                ! the actively turbulent boundary layer to help set the EPBL length scale.</span>
<span id="L2192">EPBL_TRANSITION_SCALE = 0.01    !   [nondim] default = 0.1</span>
<span id="L2193">                                ! A scale for the mixing length in the transition layer at the edge of the</span>
<span id="L2194">                                ! boundary layer as a fraction of the boundary layer thickness.</span>
<span id="L2195">MLD_ITERATION_GUESS = False     !   [Boolean] default = False</span>
<span id="L2196">                                ! If true, use the previous timestep MLD as a first guess in the MLD iteration,</span>
<span id="L2197">                                ! otherwise use half the ocean depth as the first guess of the boundary layer</span>
<span id="L2198">                                ! depth.  The default is false to facilitate reproducibility.</span>
<span id="L2199">EPBL_MLD_TOLERANCE = 1.0        !   [meter] default = 1.0</span>
<span id="L2200">                                ! The tolerance for the iteratively determined mixed layer depth.  This is only</span>
<span id="L2201">                                ! used with USE_MLD_ITERATION.</span>
<span id="L2202">EPBL_MLD_BISECTION = False      !   [Boolean] default = False</span>
<span id="L2203">                                ! If true, use bisection with the iterative determination of the self-consistent</span>
<span id="L2204">                                ! mixed layer depth.  Otherwise use the false position after a maximum and</span>
<span id="L2205">                                ! minimum bound have been evaluated and the returned value or bisection before</span>
<span id="L2206">                                ! this.</span>
<span id="L2207">EPBL_MLD_ITER_BUG = True        !   [Boolean] default = True</span>
<span id="L2208">                                ! If true, use buggy logic that gives the wrong bounds for the next iteration</span>
<span id="L2209">                                ! when successive guesses increase by exactly EPBL_MLD_TOLERANCE.</span>
<span id="L2210">EPBL_MLD_MAX_ITS = 20           ! default = 20</span>
<span id="L2211">                                ! The maximum number of iterations that can be used to find a self-consistent</span>
<span id="L2212">                                ! mixed layer depth.  If EPBL_MLD_BISECTION is true, the maximum number of</span>
<span id="L2213">                                ! iterations needed is set by Depth/2^MAX_ITS &lt; EPBL_MLD_TOLERANCE.</span>
<span id="L2214">EPBL_MIN_MIX_LEN = 0.0          !   [meter] default = 0.0</span>
<span id="L2215">                                ! The minimum mixing length scale that will be used by ePBL.  The default (0)</span>
<span id="L2216">                                ! does not set a minimum.</span>
<span id="L2217">MIX_LEN_EXPONENT = 1.0          !   [nondim] default = 2.0</span>
<span id="L2218">                                ! The exponent applied to the ratio of the distance to the MLD and the MLD depth</span>
<span id="L2219">                                ! which determines the shape of the mixing length. This is only used if</span>
<span id="L2220">                                ! USE_MLD_ITERATION is True.</span>
<span id="L2221">EPBL_VEL_SCALE_SCHEME = &quot;CUBE_ROOT_TKE&quot; ! default = &quot;CUBE_ROOT_TKE&quot;</span>
<span id="L2222">                                ! Selects the method for translating TKE into turbulent velocities. Valid values</span>
<span id="L2223">                                ! are:</span>
<span id="L2224">                                !    CUBE_ROOT_TKE  - A constant times the cube root of remaining TKE.</span>
<span id="L2225">                                !    REICHL_H18 - Use the scheme based on a combination of w* and v* as</span>
<span id="L2226">                                !                 documented in Reichl &amp; Hallberg, 2018.</span>
<span id="L2227">WSTAR_USTAR_COEF = 1.0          !   [nondim] default = 1.0</span>
<span id="L2228">                                ! A ratio relating the efficiency with which convectively released energy is</span>
<span id="L2229">                                ! converted to a turbulent velocity, relative to mechanically forced TKE. Making</span>
<span id="L2230">                                ! this larger increases the BL diffusivity</span>
<span id="L2231">EPBL_VEL_SCALE_FACTOR = 1.0     !   [nondim] default = 1.0</span>
<span id="L2232">                                ! An overall nondimensional scaling factor for wT. Making this larger increases</span>
<span id="L2233">                                ! the PBL diffusivity.</span>
<span id="L2234">VSTAR_SURF_FAC = 1.2            !   [nondim] default = 1.2</span>
<span id="L2235">                                ! The proportionality times ustar to set vstar at the surface.</span>
<span id="L2236">EPBL_BBL_EFFIC = 0.0            !   [nondim] default = 0.0</span>
<span id="L2237">                                ! The efficiency of bottom boundary layer mixing via ePBL.  Setting this to a</span>
<span id="L2238">                                ! value that is greater than 0 to enable bottom boundary layer mixing from EPBL.</span>
<span id="L2239">EPBL_BBL_TIDAL_EFFIC = 0.0      !   [nondim] default = 0.0</span>
<span id="L2240">                                ! The efficiency of bottom boundary layer mixing via ePBL driven by the bottom</span>
<span id="L2241">                                ! drag dissipation of tides, as provided in fluxes%BBL_tidal_dis.</span>
<span id="L2242">USE_LA_LI2016 = True            !   [Boolean] default = False</span>
<span id="L2243">                                ! A logical to use the Li et al. 2016 (submitted) formula to determine the</span>
<span id="L2244">                                ! Langmuir number.</span>
<span id="L2245">EPBL_LANGMUIR_SCHEME = &quot;ADDITIVE&quot; ! default = &quot;NONE&quot;</span>
<span id="L2246">                                ! EPBL_LANGMUIR_SCHEME selects the method for including Langmuir turbulence.</span>
<span id="L2247">                                ! Valid values are:</span>
<span id="L2248">                                !    NONE     - Do not do any extra mixing due to Langmuir turbulence</span>
<span id="L2249">                                !    RESCALE  - Use a multiplicative rescaling of mstar to account for Langmuir</span>
<span id="L2250">                                !      turbulence</span>
<span id="L2251">                                !    ADDITIVE - Add a Langmuir turbulence contribution to mstar to other</span>
<span id="L2252">                                !      contributions</span>
<span id="L2253">LT_ENHANCE_COEF = 0.044         !   [nondim] default = 0.447</span>
<span id="L2254">                                ! Coefficient for Langmuir enhancement of mstar</span>
<span id="L2255">LT_ENHANCE_EXP = -1.5           !   [nondim] default = -1.33</span>
<span id="L2256">                                ! Exponent for Langmuir enhancement of mstar</span>
<span id="L2257">LT_MOD_LAC1 = 0.0               !   [nondim] default = -0.87</span>
<span id="L2258">                                ! Coefficient for modification of Langmuir number due to MLD approaching Ekman</span>
<span id="L2259">                                ! depth.</span>
<span id="L2260">LT_MOD_LAC2 = 0.0               !   [nondim] default = 0.0</span>
<span id="L2261">                                ! Coefficient for modification of Langmuir number due to MLD approaching stable</span>
<span id="L2262">                                ! Obukhov depth.</span>
<span id="L2263">LT_MOD_LAC3 = 0.0               !   [nondim] default = 0.0</span>
<span id="L2264">                                ! Coefficient for modification of Langmuir number due to MLD approaching</span>
<span id="L2265">                                ! unstable Obukhov depth.</span>
<span id="L2266">LT_MOD_LAC4 = 0.0               !   [nondim] default = 0.95</span>
<span id="L2267">                                ! Coefficient for modification of Langmuir number due to ratio of Ekman to</span>
<span id="L2268">                                ! stable Obukhov depth.</span>
<span id="L2269">LT_MOD_LAC5 = 0.22              !   [nondim] default = 0.95</span>
<span id="L2270">                                ! Coefficient for modification of Langmuir number due to ratio of Ekman to</span>
<span id="L2271">                                ! unstable Obukhov depth.</span>
<span id="L2272">EPBL_EQD_DIFFUSIVITY_SHAPE = False !   [nondim] default = False</span>
<span id="L2273">                                ! Logical flag for activating ML equation for shape function that uses forcing</span>
<span id="L2274">                                ! to change its structure.</span>
<span id="L2275">EPBL_EQD_DIFFUSIVITY_VELOCITY = False !   [nondim] default = False</span>
<span id="L2276">                                ! Logical flag for activating ML equation discovery for velocity scale</span>
<span id="L2277">EPBL_EQD_DIFFUSIVITY_VELOCITY_H = False !   [nondim] default = False</span>
<span id="L2278">                                ! Logical flag for activating ML equation discovery for velocity scale with h as</span>
<span id="L2279">                                ! input</span>
<span id="L2280">EPBL_OPTIONS_DIFF = 0           ! default = 0</span>
<span id="L2281">                                ! If positive, this is a coded integer indicating a pair of settings whose</span>
<span id="L2282">                                ! differences are diagnosed in a passive diagnostic mode  via extra calls to</span>
<span id="L2283">                                ! ePBL_column.  If this is 0 or negative no extra calls occur.</span>
<span id="L2284">!EPBL_USTAR_MIN = 1.45842E-18   !   [m s-1]</span>
<span id="L2285">                                ! The (tiny) minimum friction velocity used within the ePBL code, derived from</span>
<span id="L2286">                                ! OMEGA and ANGSTROM.</span>
<span id="L2287"></span>
<span id="L2288">! === module MOM_regularize_layers ===</span>
<span id="L2289">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L2290">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L2291">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L2292"></span>
<span id="L2293">! === module MOM_opacity ===</span>
<span id="L2294">OPACITY_SCHEME = &quot;MANIZZA_05&quot;   ! default = &quot;MANIZZA_05&quot;</span>
<span id="L2295">                                ! This character string specifies how chlorophyll concentrations are translated</span>
<span id="L2296">                                ! into opacities. Currently valid options include:</span>
<span id="L2297">                                !        MANIZZA_05 - Use Manizza et al., GRL, 2005.</span>
<span id="L2298">                                !        MOREL_88 - Use Morel, JGR, 1988.</span>
<span id="L2299">                                !        OHLMANN_03 - Use Ohlmann, J Clim, 2003. (only use if dz(1)&gt;2.0m)</span>
<span id="L2300">BLUE_FRAC_SW = 0.5              !   [nondim] default = 0.5</span>
<span id="L2301">                                ! The fraction of the penetrating shortwave radiation that is in the blue band.</span>
<span id="L2302">PEN_SW_NBANDS = 3               ! default = 1</span>
<span id="L2303">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L2304">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L2305">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L2306">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L2307">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L2308">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L2309">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L2310">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L2311">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L2312">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L2313">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L2314">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L2315">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L2316">OPACITY_VALUES_MANIZZA = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0 !   [m-1] default = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0</span>
<span id="L2317">                                ! Pairs of opacity coefficients for blue, red and near-infrared radiation with</span>
<span id="L2318">                                ! parameterizations following the functional form from Manizza et al., GRL 2005,</span>
<span id="L2319">                                ! namely in the form opacity = coef_1 + coef_2 * chl**pow for each band.</span>
<span id="L2320">                                ! Although coefficients are set for 3 bands, more or less bands may actually be</span>
<span id="L2321">                                ! used, with extra bands following the same properties as band 3.</span>
<span id="L2322">CHOROPHYLL_POWER_MANIZZA = 0.674, 0.629, 0.0 !   [nondim] default = 0.674, 0.629, 0.0</span>
<span id="L2323">                                ! Powers of chlorophyll for blue, red and near-infrared radiation bands in</span>
<span id="L2324">                                ! expressions for opacity of the form opacity = coef_1 + coef_2 * chl**pow.</span>
<span id="L2325">OPACITY_BAND_WAVELENGTHS = 0.0, 550.0, 700.0, 2800.0 !   [nm] default = 0.0, 550.0, 700.0, 2800.0</span>
<span id="L2326">                                ! The bounding wavelengths for the various bands of shortwave radiation, with</span>
<span id="L2327">                                ! defaults that depend on the setting for OPACITY_SCHEME.</span>
<span id="L2328">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L2329">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L2330">                                ! muddy water.</span>
<span id="L2331"></span>
<span id="L2332">! === module MOM_tracer_advect ===</span>
<span id="L2333">TRACER_ADVECTION_SCHEME = &quot;PLM&quot; ! default = &quot;PLM&quot;</span>
<span id="L2334">                                ! The horizontal transport scheme for tracers:</span>
<span id="L2335">                                !   PLM    - Piecewise Linear Method</span>
<span id="L2336">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L2337">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L2338"></span>
<span id="L2339">! === module MOM_tracer_hor_diff ===</span>
<span id="L2340">KHTR = 50.0                     !   [m2 s-1] default = 0.0</span>
<span id="L2341">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L2342">KHTR_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L2343">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L2344">KHTR_MAX = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L2345">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L2346">                                ! activate.</span>
<span id="L2347">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L2348">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L2349">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L2350">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L2351">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L2352">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L2353">                                ! tracers to thickness mixing.</span>
<span id="L2354">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L2355">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L2356">                                ! interior.</span>
<span id="L2357">CHECK_DIFFUSIVE_CFL = True      !   [Boolean] default = False</span>
<span id="L2358">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L2359">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L2360">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L2361">MAX_TR_DIFFUSION_CFL = 2.0      !   [nondim] default = -1.0</span>
<span id="L2362">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L2363">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L2364">                                ! iterations is often this value or the next greater integer.</span>
<span id="L2365">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L2366">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L2367">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L2368">                                ! positions of the surfaces do not change</span>
<span id="L2369"></span>
<span id="L2370">! === module MOM_neutral_diffusion ===</span>
<span id="L2371">! This module implements neutral diffusion of tracers</span>
<span id="L2372">USE_NEUTRAL_DIFFUSION = True    !   [Boolean] default = False</span>
<span id="L2373">                                ! If true, enables the neutral diffusion module.</span>
<span id="L2374">NDIFF_CONTINUOUS = True         !   [Boolean] default = True</span>
<span id="L2375">                                ! If true, uses a continuous reconstruction of T and S when finding neutral</span>
<span id="L2376">                                ! surfaces along which diffusion will happen. If false, a PPM discontinuous</span>
<span id="L2377">                                ! reconstruction of T and S is done which results in a higher order routine but</span>
<span id="L2378">                                ! exacts a higher computational cost.</span>
<span id="L2379">NDIFF_REF_PRES = -1.0           !   [Pa] default = -1.0</span>
<span id="L2380">                                ! The reference pressure (Pa) used for the derivatives of the equation of state.</span>
<span id="L2381">                                ! If negative (default), local pressure is used.</span>
<span id="L2382">NDIFF_INTERIOR_ONLY = False     !   [Boolean] default = False</span>
<span id="L2383">                                ! If true, only applies neutral diffusion in the ocean interior.That is, the</span>
<span id="L2384">                                ! algorithm will exclude the surface and bottomboundary layers.</span>
<span id="L2385">NDIFF_USE_UNMASKED_TRANSPORT_BUG = False !   [Boolean] default = False</span>
<span id="L2386">                                ! If true, use an older form for the accumulation of neutral-diffusion</span>
<span id="L2387">                                ! transports that were unmasked, as used prior to Jan 2018. This is not</span>
<span id="L2388">                                ! recommended.</span>
<span id="L2389">NDIFF_ANSWER_DATE = 99991231    ! default = 99991231</span>
<span id="L2390">                                ! The vintage of the order of arithmetic to use for the neutral diffusion.</span>
<span id="L2391">                                ! Values of 20240330 or below recover the answers from the original form of the</span>
<span id="L2392">                                ! neutral diffusion code, while higher values use mathematically equivalent</span>
<span id="L2393">                                ! expressions that recover rotational symmetry.</span>
<span id="L2394"></span>
<span id="L2395">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L2396">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L2397">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L2398">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L2399">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L2400">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L2401">                                ! error rather than issue a WARNING.</span>
<span id="L2402"></span>
<span id="L2403">! === module MOM_sum_output ===</span>
<span id="L2404">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L2405">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L2406">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L2407">                                ! dramatically.</span>
<span id="L2408">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L2409">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L2410">                                ! are written.</span>
<span id="L2411">MAXTRUNC = 10000                !   [truncations save_interval-1] default = 0</span>
<span id="L2412">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L2413">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L2414">                                ! to stop if there is any truncation of velocities.</span>
<span id="L2415">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L2416">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L2417">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L2418">                                ! 10*MAXVEL^2.</span>
<span id="L2419">MAXVEL = 6.0                    !   [m s-1] default = 3.0E+08</span>
<span id="L2420">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L2421">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L2422">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L2423">DATE_STAMPED_STDOUT = True      !   [Boolean] default = True</span>
<span id="L2424">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L2425">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L2426">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L2427">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L2428">                                ! The time unit in seconds a number of input fields</span>
<span id="L2429">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L2430">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L2431">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L2432">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L2433">                                ! file.</span>
<span id="L2434">ENERGYSAVEDAYS = 1.0            !   [days] default = 1.0</span>
<span id="L2435">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L2436">                                ! other globally summed diagnostics.</span>
<span id="L2437">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L2438">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L2439">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L2440">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L2441"></span>
<span id="L2442">! === module ocean_stochastics_init ===</span>
<span id="L2443">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L2444">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L2445">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L2446">                                ! UFS model only.</span>
<span id="L2447">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L2448">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L2449">                                ! energy backscatter scheme.</span>
<span id="L2450">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L2451">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L2452">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L2453">                                ! namelist in the UFS model only.</span>
<span id="L2454"></span>
<span id="L2455">! === module ocean_model_init ===</span>
<span id="L2456">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L2457">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L2458">                                ! and thermodynamics.  If false, the two phases are advanced with separate</span>
<span id="L2459">                                ! calls.</span>
<span id="L2460">RESTART_CONTROL = 1             ! default = 1</span>
<span id="L2461">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L2462">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file.  A</span>
<span id="L2463">                                ! restart file will be saved at the end of the run segment for any non-negative</span>
<span id="L2464">                                ! value.</span>
<span id="L2465">OCEAN_SURFACE_STAGGER = &quot;A&quot;     ! default = &quot;C&quot;</span>
<span id="L2466">                                ! A case-insensitive character string to indicate the staggering of the surface</span>
<span id="L2467">                                ! velocity field that is returned to the coupler.  Valid values include &#x27;A&#x27;,</span>
<span id="L2468">                                ! &#x27;B&#x27;, or &#x27;C&#x27;.</span>
<span id="L2469">EPS_OMESH = 1.0E-13             !   [degrees] default = 1.0E-04</span>
<span id="L2470">                                ! Maximum allowable difference between ESMF mesh and MOM6 domain coordinates in</span>
<span id="L2471">                                ! nuopc cap.</span>
<span id="L2472">RESTORE_SALINITY = False        !   [Boolean] default = False</span>
<span id="L2473">                                ! If true, the coupled driver will add a globally-balanced fresh-water flux that</span>
<span id="L2474">                                ! drives sea-surface salinity toward specified values.</span>
<span id="L2475">RESTORE_TEMPERATURE = False     !   [Boolean] default = False</span>
<span id="L2476">                                ! If true, the coupled driver will add a heat flux that drives sea-surface</span>
<span id="L2477">                                ! temperature toward specified values.</span>
<span id="L2478">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L2479">                                ! If true, enables the ice shelf model.</span>
<span id="L2480">ICEBERGS_APPLY_RIGID_BOUNDARY = False !   [Boolean] default = False</span>
<span id="L2481">                                ! If true, allows icebergs to change boundary condition felt by ocean</span>
<span id="L2482">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L2483">                                ! If true, enables surface wave modules.</span>
<span id="L2484"></span>
<span id="L2485">! === module MOM_surface_forcing_nuopc ===</span>
<span id="L2486">LATENT_HEAT_FUSION = 3.337E+05  !   [J/kg] default = 3.34E+05</span>
<span id="L2487">                                ! The latent heat of fusion.</span>
<span id="L2488">LATENT_HEAT_VAPORIZATION = 2.501E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L2489">                                ! The latent heat of fusion.</span>
<span id="L2490">MAX_P_SURF = -1.0               !   [Pa] default = -1.0</span>
<span id="L2491">                                ! The maximum surface pressure that can be exerted by the atmosphere and</span>
<span id="L2492">                                ! floating sea-ice or ice shelves. This is needed because the FMS coupling</span>
<span id="L2493">                                ! structure does not limit the water that can be frozen out of the ocean and the</span>
<span id="L2494">                                ! ice-ocean heat fluxes are treated explicitly.  No limit is applied if a</span>
<span id="L2495">                                ! negative value is used.</span>
<span id="L2496">ADJUST_NET_SRESTORE_TO_ZERO = False !   [Boolean] default = False</span>
<span id="L2497">                                ! If true, adjusts the salinity restoring seen to zero whether restoring is via</span>
<span id="L2498">                                ! a salt flux or virtual precip.</span>
<span id="L2499">ADJUST_NET_SRESTORE_BY_SCALING = False !   [Boolean] default = False</span>
<span id="L2500">                                ! If true, adjustments to salt restoring to achieve zero net are made by scaling</span>
<span id="L2501">                                ! values without moving the zero contour.</span>
<span id="L2502">ADJUST_NET_FRESH_WATER_TO_ZERO = False !   [Boolean] default = False</span>
<span id="L2503">                                ! If true, adjusts the net fresh-water forcing seen by the ocean (including</span>
<span id="L2504">                                ! restoring) to zero.</span>
<span id="L2505">ADJUST_NET_FRESH_WATER_BY_SCALING = False !   [Boolean] default = False</span>
<span id="L2506">                                ! If true, adjustments to net fresh water to achieve zero net are made by</span>
<span id="L2507">                                ! scaling values without moving the zero contour.</span>
<span id="L2508">ICE_SALT_CONCENTRATION = 0.005  !   [kg/kg] default = 0.005</span>
<span id="L2509">                                ! The assumed sea-ice salinity needed to reverse engineer the melt flux (or</span>
<span id="L2510">                                ! ice-ocean fresh-water flux).</span>
<span id="L2511">USE_LIMITED_PATM_SSH = True     !   [Boolean] default = True</span>
<span id="L2512">                                ! If true, return the sea surface height with the correction for the atmospheric</span>
<span id="L2513">                                ! (and sea-ice) pressure limited by max_p_surf instead of the full atmospheric</span>
<span id="L2514">                                ! pressure.</span>
<span id="L2515">WIND_STAGGER = &quot;A&quot;              ! default = &quot;C&quot;</span>
<span id="L2516">                                ! A case-insensitive character string to indicate the staggering of the input</span>
<span id="L2517">                                ! wind stress field.  Valid values are &#x27;A&#x27;, &#x27;B&#x27;, or &#x27;C&#x27;.</span>
<span id="L2518">WIND_STRESS_MULTIPLIER = 1.0    !   [nondim] default = 1.0</span>
<span id="L2519">                                ! A factor multiplying the wind-stress given to the ocean by the coupler. This</span>
<span id="L2520">                                ! is used for testing and should be =1.0 for any production runs.</span>
<span id="L2521">ENTHALPY_FROM_COUPLER = False   !   [Boolean] default = False</span>
<span id="L2522">                                ! If True, the heat (enthalpy) associated with mass entering/leaving the ocean</span>
<span id="L2523">                                ! is provided via coupler.</span>
<span id="L2524">CD_TIDES = 1.0E-04              !   [nondim] default = 1.0E-04</span>
<span id="L2525">                                ! The drag coefficient that applies to the tides.</span>
<span id="L2526">READ_TIDEAMP = False            !   [Boolean] default = False</span>
<span id="L2527">                                ! If true, read a file (given by TIDEAMP_FILE) containing the tidal amplitude</span>
<span id="L2528">                                ! with INT_TIDE_DISSIPATION.</span>
<span id="L2529">UTIDE = 0.0                     !   [m s-1] default = 0.0</span>
<span id="L2530">                                ! The constant tidal amplitude used with INT_TIDE_DISSIPATION.</span>
<span id="L2531">READ_GUST_2D = False            !   [Boolean] default = False</span>
<span id="L2532">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L2533">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L2534">                                ! The background gustiness in the winds.</span>
<span id="L2535">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L2536">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L2537">                                ! velocity</span>
<span id="L2538">USE_RIGID_SEA_ICE = False       !   [Boolean] default = False</span>
<span id="L2539">                                ! If true, sea-ice is rigid enough to exert a nonhydrostatic pressure that</span>
<span id="L2540">                                ! resist vertical motion.</span>
<span id="L2541">ALLOW_ICEBERG_FLUX_DIAGNOSTICS = False !   [Boolean] default = False</span>
<span id="L2542">                                ! If true, makes available diagnostics of fluxes from icebergs as seen by MOM6.</span>
<span id="L2543">ALLOW_GLC_RUNOFF_DIAGNOSTICS = False !   [Boolean] default = False</span>
<span id="L2544">                                ! If true, makes available diagnostics of separate glacier runoff fluxesas seen</span>
<span id="L2545">                                ! by MOM6.</span>
<span id="L2546">ALLOW_FLUX_ADJUSTMENTS = False  !   [Boolean] default = False</span>
<span id="L2547">                                ! If true, allows flux adjustments to specified via the data_table using the</span>
<span id="L2548">                                ! component name &#x27;OCN&#x27;.</span>
<span id="L2549">LIQUID_RUNOFF_FROM_DATA = False !   [Boolean] default = False</span>
<span id="L2550">                                ! If true, allows liquid river runoff to be specified via the data_table using</span>
<span id="L2551">                                ! the component name &#x27;OCN&#x27;.</span>
<span id="L2552"></span>
<span id="L2553">! === module MOM_restart ===</span>
<span id="L2554">WAVE_INTERFACE_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L2555">                                ! The vintage of the order of arithmetic and expressions in the surface wave</span>
<span id="L2556">                                ! calculations.  Values below 20230101 recover the answers from the end of 2022,</span>
<span id="L2557">                                ! while higher values use updated and more robust forms of the same expressions:</span>
<span id="L2558">                                !    &lt;  20230101 - Original answers for wave interface routines</span>
<span id="L2559">                                !    &gt;= 20230101 - More robust expressions for Update_Stokes_Drift</span>
<span id="L2560">                                !    &gt;= 20230102 - More robust expressions for get_StokesSL_LiFoxKemper</span>
<span id="L2561">                                !    &gt;= 20230103 - More robust expressions for ust_2_u10_coare3p5</span>
<span id="L2562">LA_DEPTH_RATIO = 0.04           !   [nondim] default = 0.04</span>
<span id="L2563">                                ! The depth (normalized by BLD) to average Stokes drift over in Langmuir number</span>
<span id="L2564">                                ! calculation, where La = sqrt(ust/Stokes).</span>
<span id="L2565">LA_DEPTH_MIN = 0.1              !   [m] default = 0.1</span>
<span id="L2566">                                ! The minimum depth over which to average the Stokes drift in the Langmuir</span>
<span id="L2567">                                ! number calculation.</span>
<span id="L2568">VISCOSITY_AIR = 1.0E-06         !   [m2 s-1] default = 1.0E-06</span>
<span id="L2569">                                ! A typical viscosity of air at sea level, as used in wave calculations</span>
<span id="L2570">VON_KARMAN_WAVES = 0.4          !   [nondim] default = 0.4</span>
<span id="L2571">                                ! The value the von Karman constant as used for surface wave calculations.</span>
<span id="L2572">RHO_AIR = 1.225                 !   [kg m-3] default = 1.225</span>
<span id="L2573">                                ! A typical density of air at sea level, as used in wave calculations</span>
<span id="L2574">RHO_SFC_WAVES = 1035.0          !   [kg m-3] default = 1035.0</span>
<span id="L2575">                                ! A typical surface density of seawater, as used in wave calculations in</span>
<span id="L2576">                                ! comparison with the density of air.  The default is RHO_0.</span>
<span id="L2577">WAVE_HEIGHT_SCALE_FACTOR = 0.0246 !   [s2 m-1] default = 0.0246</span>
<span id="L2578">                                ! A factor relating the square of the 10 m wind speed to the significant wave</span>
<span id="L2579">                                ! height, with a default value based on the Pierson-Moskowitz spectrum.</span>
<span id="L2580">CHARNOCK_MIN = 0.028            !   [nondim] default = 0.028</span>
<span id="L2581">                                ! The minimum value of the Charnock coefficient, which relates the square of the</span>
<span id="L2582">                                ! air friction velocity divided by the gravitational acceleration to the wave</span>
<span id="L2583">                                ! roughness length.</span>
<span id="L2584">CHARNOCK_SLOPE_U10 = 0.0017     !   [s m-1] default = 0.0017</span>
<span id="L2585">                                ! The partial derivative of the Charnock coefficient with the 10 m wind speed.</span>
<span id="L2586">                                ! Note that in eq. 13 of the Edson et al. 2013 describing the COARE 3.5 bulk</span>
<span id="L2587">                                ! flux algorithm, this slope is given as 0.017.  However, 0.0017 reproduces the</span>
<span id="L2588">                                ! curve in their figure 6, so that is the default value used in MOM6.</span>
<span id="L2589">CHARNOCK_0_WIND_INTERCEPT = -0.005 !   [nondim] default = -0.005</span>
<span id="L2590">                                ! The intercept of the fit for the Charnock coefficient in the limit of no wind.</span>
<span id="L2591">                                ! Note that this can be negative because CHARNOCK_MIN will keep the final value</span>
<span id="L2592">                                ! for the Charnock coefficient from being from being negative.</span>
<span id="L2593"></span>
<span id="L2594">! === module MOM_file_parser ===</span>
<span id="L2595">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L2596">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L2597">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L2598">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L2599">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L2600">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L2601">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L2602">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L2603">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L2604">                                ! MOM_parameter_doc.short .</span>
</pre>
