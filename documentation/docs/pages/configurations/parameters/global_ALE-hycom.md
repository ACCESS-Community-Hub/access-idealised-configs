---
search:
  exclude: true
---

# global_ALE-hycom: MOM_parameter_doc.all

Every MOM6 parameter of the tested run of [global_ALE-hycom](../mom6examples/global_ALE-hycom.md), as MOM6 wrote it to `MOM_parameter_doc.all` in the run's output folder. Line numbers match the file.

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
<span id="L18">DIABATIC_FIRST = True           !   [Boolean] default = False</span>
<span id="L19">                                ! If true, apply diabatic and thermodynamic processes, including buoyancy</span>
<span id="L20">                                ! forcing and mass gain or loss, before stepping the dynamics forward.</span>
<span id="L21">USE_CONTEMP_ABSSAL = False      !   [Boolean] default = False</span>
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
<span id="L75">DT_THERM = 7200.0               !   [s] default = 3600.0</span>
<span id="L76">                                ! The thermodynamic time step. Ideally DT_THERM should be an integer multiple of</span>
<span id="L77">                                ! DT and of DT_TRACER_ADVECT and less than the forcing or coupling time-step.</span>
<span id="L78">                                ! However, if THERMO_SPANS_COUPLING is true, DT_THERM can be an integer multiple</span>
<span id="L79">                                ! of the coupling timestep. By default DT_THERM is set to DT.</span>
<span id="L80">THERMO_SPANS_COUPLING = False   !   [Boolean] default = False</span>
<span id="L81">                                ! If true, the MOM will take thermodynamic timesteps that can be longer than the</span>
<span id="L82">                                ! coupling timestep. The actual thermodynamic timestep that is used in this case</span>
<span id="L83">                                ! is the largest integer multiple of the coupling timestep that is less than or</span>
<span id="L84">                                ! equal to DT_THERM.</span>
<span id="L85">DT_TRACER_ADVECT = 7200.0       !   [s] default = 7200.0</span>
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
<span id="L112">HFREEZE = -1.0                  !   [m] default = -1.0</span>
<span id="L113">                                ! If HFREEZE &gt; 0, melt potential will be computed. The actual depth over which</span>
<span id="L114">                                ! melt potential is computed will be min(HFREEZE, OBLD), where OBLD is the</span>
<span id="L115">                                ! boundary layer depth. If HFREEZE &lt;= 0 (default), melt potential will not be</span>
<span id="L116">                                ! computed.</span>
<span id="L117">INTERPOLATE_P_SURF = False      !   [Boolean] default = False</span>
<span id="L118">                                ! If true, linearly interpolate the surface pressure over the coupling time</span>
<span id="L119">                                ! step, using the specified value at the end of the step.</span>
<span id="L120">DTBT_RESET_PERIOD = 0.0         !   [s] default = 7200.0</span>
<span id="L121">                                ! The period between recalculations of DTBT (if DTBT &lt;= 0). If DTBT_RESET_PERIOD</span>
<span id="L122">                                ! is negative, DTBT is set based only on information available at</span>
<span id="L123">                                ! initialization.  If 0, DTBT will be set every dynamics time step. The default</span>
<span id="L124">                                ! is set by DT_THERM.  This is only used if SPLIT is true.</span>
<span id="L125">FRAZIL = True                   !   [Boolean] default = False</span>
<span id="L126">                                ! If true, water freezes if it gets too cold, and the accumulated heat deficit</span>
<span id="L127">                                ! is returned in the surface state.  FRAZIL is only used if</span>
<span id="L128">                                ! ENABLE_THERMODYNAMICS is true.</span>
<span id="L129">DO_GEOTHERMAL = True            !   [Boolean] default = False</span>
<span id="L130">                                ! If true, apply geothermal heating.</span>
<span id="L131">BOUND_SALINITY = True           !   [Boolean] default = False</span>
<span id="L132">                                ! If true, limit salinity to being positive. (The sea-ice model may ask for more</span>
<span id="L133">                                ! salt than is available and drive the salinity negative otherwise.)</span>
<span id="L134">MIN_SALINITY = 0.01             !   [PPT] default = 0.0</span>
<span id="L135">                                ! The minimum value of salinity when BOUND_SALINITY=True.</span>
<span id="L136">SALINITY_UNDERFLOW = 0.0        !   [PPT] default = 0.0</span>
<span id="L137">                                ! A tiny value of salinity below which the it is set to 0.  For reference, one</span>
<span id="L138">                                ! molecule of salt per square meter of ocean is of order 1e-29 ppt.</span>
<span id="L139">TEMPERATURE_UNDERFLOW = 0.0     !   [degC] default = 0.0</span>
<span id="L140">                                ! A tiny magnitude of temperatures below which they are set to 0.</span>
<span id="L141">C_P = 3925.0                    !   [J kg-1 K-1] default = 3991.86795711963</span>
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
<span id="L169">BAD_VAL_SSH_MAX = 20.0          !   [m] default = 20.0</span>
<span id="L170">                                ! The value of SSH above which a bad value message is triggered, if</span>
<span id="L171">                                ! CHECK_BAD_SURFACE_VALS is true.</span>
<span id="L172">BAD_VAL_SSS_MAX = 45.0          !   [PPT] default = 45.0</span>
<span id="L173">                                ! The value of SSS above which a bad value message is triggered, if</span>
<span id="L174">                                ! CHECK_BAD_SURFACE_VALS is true.</span>
<span id="L175">BAD_VAL_SST_MAX = 45.0          !   [deg C] default = 45.0</span>
<span id="L176">                                ! The value of SST above which a bad value message is triggered, if</span>
<span id="L177">                                ! CHECK_BAD_SURFACE_VALS is true.</span>
<span id="L178">BAD_VAL_SST_MIN = -2.1          !   [deg C] default = -2.1</span>
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
<span id="L190">SAVE_INITIAL_CONDS = True       !   [Boolean] default = False</span>
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
<span id="L203">ICE_SHELF = False               !   [Boolean] default = False</span>
<span id="L204">                                ! If true, enables the ice shelf model.</span>
<span id="L205">USE_PARTICLES = False           !   [Boolean] default = False</span>
<span id="L206">                                ! If true, use the particles package.</span>
<span id="L207">USE_UH_PARTICLES = False        !   [Boolean] default = False</span>
<span id="L208">                                ! If true, use the uh velocity in the particles package.</span>
<span id="L209">ENSEMBLE_OCEAN = False          !   [Boolean] default = False</span>
<span id="L210">                                ! If False, The model is being run in serial mode as a single realization. If</span>
<span id="L211">                                ! True, The current model realization is part of a larger ensemble and at the</span>
<span id="L212">                                ! end of step MOM, we will perform a gather of the ensemble members for</span>
<span id="L213">                                ! statistical evaluation and/or data assimilation.</span>
<span id="L214">HOMOGENIZE_FORCINGS = False     !   [Boolean] default = False</span>
<span id="L215">                                ! If True, homogenize the forces and fluxes.</span>
<span id="L216"></span>
<span id="L217">! === module MOM_domains ===</span>
<span id="L218">REENTRANT_X = True              !   [Boolean] default = True</span>
<span id="L219">                                ! If true, the domain is zonally reentrant.</span>
<span id="L220">REENTRANT_Y = False             !   [Boolean] default = False</span>
<span id="L221">                                ! If true, the domain is meridionally reentrant.</span>
<span id="L222">TRIPOLAR_N = True               !   [Boolean] default = False</span>
<span id="L223">                                ! Use tripolar connectivity at the northern edge of the domain.  With</span>
<span id="L224">                                ! TRIPOLAR_N, NIGLOBAL must be even.</span>
<span id="L225">NIGLOBAL = 360                  !</span>
<span id="L226">                                ! The total number of thickness grid points in the x-direction in the physical</span>
<span id="L227">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L228">NJGLOBAL = 210                  !</span>
<span id="L229">                                ! The total number of thickness grid points in the y-direction in the physical</span>
<span id="L230">                                ! domain. With STATIC_MEMORY_ this is set in MOM_memory.h at compile time.</span>
<span id="L231">NIHALO = 4                      ! default = 4</span>
<span id="L232">                                ! The number of halo points on each side in the x-direction.  How this is set</span>
<span id="L233">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L234">NJHALO = 4                      ! default = 4</span>
<span id="L235">                                ! The number of halo points on each side in the y-direction.  How this is set</span>
<span id="L236">                                ! varies with the calling component and static or dynamic memory configuration.</span>
<span id="L237"></span>
<span id="L238">! === module MOM_hor_index ===</span>
<span id="L239">! Sets the horizontal array index types.</span>
<span id="L240"></span>
<span id="L241">! === module MOM_grid ===</span>
<span id="L242">! Parameters providing information about the lateral grid.</span>
<span id="L243">REFERENCE_HEIGHT = 0.0          !   [m] default = 0.0</span>
<span id="L244">                                ! A reference value for geometric height fields, such as bathyT.</span>
<span id="L245"></span>
<span id="L246">! === module MOM_fixed_initialization ===</span>
<span id="L247">INPUTDIR = &quot;INPUT&quot;              ! default = &quot;.&quot;</span>
<span id="L248">                                ! The directory in which input files are found.</span>
<span id="L249"></span>
<span id="L250">! === module MOM_grid_init ===</span>
<span id="L251">GRID_CONFIG = &quot;mosaic&quot;          !</span>
<span id="L252">                                ! A character string that determines the method for defining the horizontal</span>
<span id="L253">                                ! grid.  Current options are:</span>
<span id="L254">                                !     mosaic - read the grid from a mosaic (supergrid)</span>
<span id="L255">                                !              file set by GRID_FILE.</span>
<span id="L256">                                !     cartesian - use a (flat) Cartesian grid.</span>
<span id="L257">                                !     spherical - use a simple spherical grid.</span>
<span id="L258">                                !     mercator - use a Mercator spherical grid.</span>
<span id="L259">GRID_FILE = &quot;ocean_hgrid.nc&quot;    !</span>
<span id="L260">                                ! Name of the file from which to read horizontal grid data.</span>
<span id="L261">USE_TRIPOLAR_GEOLONB_BUG = False !   [Boolean] default = False</span>
<span id="L262">                                ! If true, use older code that incorrectly sets the longitude in some points</span>
<span id="L263">                                ! along the tripolar fold to be off by 360 degrees.</span>
<span id="L264">RAD_EARTH = 6.378E+06           !   [m] default = 6.378E+06</span>
<span id="L265">                                ! The radius of the Earth.</span>
<span id="L266">TOPO_CONFIG = &quot;file&quot;            !</span>
<span id="L267">                                ! This specifies how bathymetry is specified:</span>
<span id="L268">                                !     file - read bathymetric information from the file</span>
<span id="L269">                                !       specified by (TOPO_FILE).</span>
<span id="L270">                                !     flat - flat bottom set to MAXIMUM_DEPTH.</span>
<span id="L271">                                !     bowl - an analytically specified bowl-shaped basin</span>
<span id="L272">                                !       ranging between MAXIMUM_DEPTH and MINIMUM_DEPTH.</span>
<span id="L273">                                !     spoon - a similar shape to &#x27;bowl&#x27;, but with an vertical</span>
<span id="L274">                                !       wall at the southern face.</span>
<span id="L275">                                !     halfpipe - a zonally uniform channel with a half-sine</span>
<span id="L276">                                !       profile in the meridional direction.</span>
<span id="L277">                                !     bbuilder - build topography from list of functions.</span>
<span id="L278">                                !     benchmark - use the benchmark test case topography.</span>
<span id="L279">                                !     Neverworld - use the Neverworld test case topography.</span>
<span id="L280">                                !     DOME - use a slope and channel configuration for the</span>
<span id="L281">                                !       DOME sill-overflow test case.</span>
<span id="L282">                                !     ISOMIP - use a slope and channel configuration for the</span>
<span id="L283">                                !       ISOMIP test case.</span>
<span id="L284">                                !     DOME2D - use a shelf and slope configuration for the</span>
<span id="L285">                                !       DOME2D gravity current/overflow test case.</span>
<span id="L286">                                !     Kelvin - flat but with rotated land mask.</span>
<span id="L287">                                !     seamount - Gaussian bump for spontaneous motion test case.</span>
<span id="L288">                                !     dumbbell - Sloshing channel with reservoirs on both ends.</span>
<span id="L289">                                !     shelfwave - exponential slope for shelfwave test case.</span>
<span id="L290">                                !     Phillips - ACC-like idealized topography used in the Phillips config.</span>
<span id="L291">                                !     dense - Denmark Strait-like dense water formation and overflow.</span>
<span id="L292">                                !     USER - call a user modified routine.</span>
<span id="L293">TOPO_FILE = &quot;topog.nc&quot;          ! default = &quot;topog.nc&quot;</span>
<span id="L294">                                ! The file from which the bathymetry is read.</span>
<span id="L295">TOPO_VARNAME = &quot;depth&quot;          ! default = &quot;depth&quot;</span>
<span id="L296">                                ! The name of the bathymetry variable in TOPO_FILE.</span>
<span id="L297">TOPO_EDITS_FILE = &quot;&quot;            ! default = &quot;&quot;</span>
<span id="L298">                                ! The file from which to read a list of i,j,z topography overrides.</span>
<span id="L299">ALLOW_LANDMASK_CHANGES = False  !   [Boolean] default = False</span>
<span id="L300">                                ! If true, allow topography overrides to change land mask.</span>
<span id="L301">MINIMUM_DEPTH = 0.5             !   [m] default = 0.0</span>
<span id="L302">                                ! If MASKING_DEPTH is unspecified, then anything shallower than MINIMUM_DEPTH is</span>
<span id="L303">                                ! assumed to be land and all fluxes are masked out. If MASKING_DEPTH is</span>
<span id="L304">                                ! specified, then all depths shallower than MINIMUM_DEPTH but deeper than</span>
<span id="L305">                                ! MASKING_DEPTH are rounded to MINIMUM_DEPTH.</span>
<span id="L306">MASKING_DEPTH = -9999.0         !   [m] default = -9999.0</span>
<span id="L307">                                ! The depth below which to mask points as land points, for which all fluxes are</span>
<span id="L308">                                ! zeroed out. MASKING_DEPTH is ignored if it has the special default value.</span>
<span id="L309">MAXIMUM_DEPTH = 6000.0          !   [m]</span>
<span id="L310">                                ! The maximum depth of the ocean.</span>
<span id="L311"></span>
<span id="L312">! === module MOM_open_boundary ===</span>
<span id="L313">! Controls where open boundaries are located, what kind of boundary condition to impose, and what data to apply,</span>
<span id="L314">! if any.</span>
<span id="L315">OBC_NUMBER_OF_SEGMENTS = 0      ! default = 0</span>
<span id="L316">                                ! The number of open boundary segments.</span>
<span id="L317">CHANNEL_CONFIG = &quot;global_1deg&quot;  ! default = &quot;none&quot;</span>
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
<span id="L330">ROTATION = &quot;2omegasinlat&quot;       ! default = &quot;2omegasinlat&quot;</span>
<span id="L331">                                ! This specifies how the Coriolis parameter is specified:</span>
<span id="L332">                                !     2omegasinlat - Use twice the planetary rotation rate</span>
<span id="L333">                                !       times the sine of latitude.</span>
<span id="L334">                                !     betaplane - Use a beta-plane or f-plane.</span>
<span id="L335">                                !     USER - call a user modified routine.</span>
<span id="L336">OMEGA = 7.2921E-05              !   [s-1] default = 7.2921E-05</span>
<span id="L337">                                ! The rotation rate of the earth.</span>
<span id="L338">GRID_ROTATION_ANGLE_BUGS = False !   [Boolean] default = False</span>
<span id="L339">                                ! If true, use an older algorithm to calculate the sine and cosines needed</span>
<span id="L340">                                ! rotate between grid-oriented directions and true north and east.  Differences</span>
<span id="L341">                                ! arise at the tripolar fold.</span>
<span id="L342"></span>
<span id="L343">! === module MOM_verticalGrid ===</span>
<span id="L344">! Parameters providing information about the vertical grid.</span>
<span id="L345">G_EARTH = 9.8                   !   [m s-2] default = 9.8</span>
<span id="L346">                                ! The gravitational acceleration of the Earth.</span>
<span id="L347">RHO_0 = 1035.0                  !   [kg m-3] default = 1035.0</span>
<span id="L348">                                ! The mean ocean density used with BOUSSINESQ true to calculate accelerations</span>
<span id="L349">                                ! and the mass for conservation properties, or with BOUSSINSEQ false to convert</span>
<span id="L350">                                ! some parameters from vertical units of m to kg m-2.</span>
<span id="L351">BOUSSINESQ = True               !   [Boolean] default = True</span>
<span id="L352">                                ! If true, make the Boussinesq approximation.</span>
<span id="L353">ANGSTROM = 1.0E-10              !   [m] default = 1.0E-10</span>
<span id="L354">                                ! The minimum layer thickness, usually one-Angstrom.</span>
<span id="L355">H_TO_M = 1.0                    !   [m H-1] default = 1.0</span>
<span id="L356">                                ! A constant that translates the model&#x27;s internal units of thickness into m.</span>
<span id="L357">NK = 50                         !   [nondim]</span>
<span id="L358">                                ! The number of model layers.</span>
<span id="L359">ADVECTION_SCHEME_VARIANCE_UNDERFLOW = 1.0E-23 !   [Conc2 (tracer dependent)] default = 1.0E-23</span>
<span id="L360">                                ! A tiny magnitude for variance used to determine when advection scheme variance</span>
<span id="L361">                                ! production is set to 0.</span>
<span id="L362"></span>
<span id="L363">! === module MOM_tracer_registry ===</span>
<span id="L364"></span>
<span id="L365">! === module MOM_EOS ===</span>
<span id="L366">EQN_OF_STATE = &quot;WRIGHT&quot;         ! default = &quot;WRIGHT_FULL&quot;</span>
<span id="L367">                                ! EQN_OF_STATE determines which ocean equation of state should be used.</span>
<span id="L368">                                ! Currently, the valid choices are &quot;LINEAR&quot;, &quot;UNESCO&quot;, &quot;JACKETT_MCD&quot;, &quot;WRIGHT&quot;,</span>
<span id="L369">                                ! &quot;WRIGHT_REDUCED&quot;, &quot;WRIGHT_FULL&quot;, &quot;NEMO&quot;, &quot;ROQUET_RHO&quot;, &quot;ROQUET_SPV&quot; and</span>
<span id="L370">                                ! &quot;TEOS10&quot;.  This is only used if USE_EOS is true.</span>
<span id="L371">USE_WRIGHT_2ND_DERIV_BUG = False !   [Boolean] default = False</span>
<span id="L372">                                ! If true, use a bug in the calculation of the second derivatives of density</span>
<span id="L373">                                ! with temperature and with temperature and pressure that causes some terms to</span>
<span id="L374">                                ! be only 2/3 of what they should be.</span>
<span id="L375">EOS_QUADRATURE = False          !   [Boolean] default = False</span>
<span id="L376">                                ! If true, always use the generic (quadrature) code code for the integrals of</span>
<span id="L377">                                ! density.</span>
<span id="L378">TFREEZE_FORM = &quot;LINEAR&quot;         ! default = &quot;LINEAR&quot;</span>
<span id="L379">                                ! TFREEZE_FORM determines which expression should be used for the freezing</span>
<span id="L380">                                ! point.  Currently, the valid choices are &quot;LINEAR&quot;, &quot;MILLERO_78&quot;, &quot;TEOS_POLY&quot;,</span>
<span id="L381">                                ! &quot;TEOS10&quot;</span>
<span id="L382">TFREEZE_S0_P0 = 0.0             !   [degC] default = 0.0</span>
<span id="L383">                                ! When TFREEZE_FORM=LINEAR, this is the freezing potential temperature at S=0,</span>
<span id="L384">                                ! P=0.</span>
<span id="L385">DTFREEZE_DS = -0.054            !   [degC ppt-1] default = -0.054</span>
<span id="L386">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L387">                                ! temperature with salinity.</span>
<span id="L388">DTFREEZE_DP = 0.0               !   [degC Pa-1] default = 0.0</span>
<span id="L389">                                ! When TFREEZE_FORM=LINEAR, this is the derivative of the freezing potential</span>
<span id="L390">                                ! temperature with pressure.</span>
<span id="L391">TFREEZE_S_IS_PRACS = True       !   [Boolean] default = True</span>
<span id="L392">                                ! When True, the model will check if the model internal salinity is practical</span>
<span id="L393">                                ! salinity.  If the model uses absolute salinity, a conversion will be applied.</span>
<span id="L394">TFREEZE_T_IS_POTT = True        !   [Boolean] default = True</span>
<span id="L395">                                ! When True, the model will check if the model internal temperature is potential</span>
<span id="L396">                                ! temperature.  If the model uses conservative temperature, a conversion will be</span>
<span id="L397">                                ! applied.</span>
<span id="L398"></span>
<span id="L399">! === module MOM_restart ===</span>
<span id="L400">PARALLEL_RESTARTFILES = True    !   [Boolean] default = False</span>
<span id="L401">                                ! If true, the IO layout is used to group processors that write to the same</span>
<span id="L402">                                ! restart file or each processor writes its own (numbered) restart file. If</span>
<span id="L403">                                ! false, a single restart file is generated combining output from all PEs.</span>
<span id="L404">RESTARTFILE = &quot;MOM.res&quot;         ! default = &quot;MOM.res&quot;</span>
<span id="L405">                                ! The name-root of the restart file.</span>
<span id="L406">MAX_FIELDS = 100                ! default = 100</span>
<span id="L407">                                ! The maximum number of restart fields that can be used.</span>
<span id="L408">RESTART_CHECKSUMS_REQUIRED = True !   [Boolean] default = True</span>
<span id="L409">                                ! If true, require the restart checksums to match and error out otherwise. Users</span>
<span id="L410">                                ! may want to avoid this comparison if for example the restarts are made from a</span>
<span id="L411">                                ! run with a different mask_table than the current run, in which case the</span>
<span id="L412">                                ! checksums will not match and cause crash.</span>
<span id="L413">RESTART_SYMMETRIC_CHECKSUMS = False !   [Boolean] default = False</span>
<span id="L414">                                ! If true, do the restart checksums on all the edge points for a non-reentrant</span>
<span id="L415">                                ! grid.  This requires that SYMMETRIC_MEMORY_ is defined at compile time.</span>
<span id="L416">RESTART_UNSIGNED_ZEROS = False  !   [Boolean] default = False</span>
<span id="L417">                                ! If true, convert any negative zeros that would be written to the restart file</span>
<span id="L418">                                ! into ordinary unsigned zeros.  This does not change answers, but it can be</span>
<span id="L419">                                ! helpful in comparing restart files after grid rotation, for example.</span>
<span id="L420">USE_FILTER = False              !   [Boolean] default = False</span>
<span id="L421">                                ! If true, use streaming band-pass filters to detect the instantaneous tidal</span>
<span id="L422">                                ! signals in the simulation.</span>
<span id="L423"></span>
<span id="L424">! === module MOM_tracer_flow_control ===</span>
<span id="L425">USE_USER_TRACER_EXAMPLE = False !   [Boolean] default = False</span>
<span id="L426">                                ! If true, use the USER_tracer_example tracer package.</span>
<span id="L427">USE_DOME_TRACER = False         !   [Boolean] default = False</span>
<span id="L428">                                ! If true, use the DOME_tracer tracer package.</span>
<span id="L429">USE_ISOMIP_TRACER = False       !   [Boolean] default = False</span>
<span id="L430">                                ! If true, use the ISOMIP_tracer tracer package.</span>
<span id="L431">USE_RGC_TRACER = False          !   [Boolean] default = False</span>
<span id="L432">                                ! If true, use the RGC_tracer tracer package.</span>
<span id="L433">USE_IDEAL_AGE_TRACER = True     !   [Boolean] default = False</span>
<span id="L434">                                ! If true, use the ideal_age_example tracer package.</span>
<span id="L435">USE_MARBL_TRACERS = False       !   [Boolean] default = False</span>
<span id="L436">                                ! If true, use the MARBL tracer package.</span>
<span id="L437">USE_REGIONAL_DYES = False       !   [Boolean] default = False</span>
<span id="L438">                                ! If true, use the regional_dyes tracer package.</span>
<span id="L439">USE_FILE_DYES = False           !   [Boolean] default = False</span>
<span id="L440">                                ! If true, use the file dyes tracer package.</span>
<span id="L441">USE_OIL_TRACER = False          !   [Boolean] default = False</span>
<span id="L442">                                ! If true, use the oil_tracer tracer package.</span>
<span id="L443">USE_ADVECTION_TEST_TRACER = False !   [Boolean] default = False</span>
<span id="L444">                                ! If true, use the advection_test_tracer tracer package.</span>
<span id="L445">USE_OCMIP2_CFC = False          !   [Boolean] default = False</span>
<span id="L446">                                ! If true, use the MOM_OCMIP2_CFC tracer package.</span>
<span id="L447">USE_CFC_CAP = False             !   [Boolean] default = False</span>
<span id="L448">                                ! If true, use the MOM_CFC_cap tracer package.</span>
<span id="L449">USE_generic_tracer = False      !   [Boolean] default = False</span>
<span id="L450">                                ! If true and _USE_GENERIC_TRACER is defined as a preprocessor macro, use the</span>
<span id="L451">                                ! MOM_generic_tracer packages.</span>
<span id="L452">USE_PSEUDO_SALT_TRACER = False  !   [Boolean] default = False</span>
<span id="L453">                                ! If true, use the pseudo salt tracer, typically run as a diagnostic.</span>
<span id="L454">USE_BOUNDARY_IMPULSE_TRACER = False !   [Boolean] default = False</span>
<span id="L455">                                ! If true, use the boundary impulse tracer.</span>
<span id="L456">USE_DYED_OBC_TRACER = False     !   [Boolean] default = False</span>
<span id="L457">                                ! If true, use the dyed_obc_tracer tracer package.</span>
<span id="L458">USE_NW2_TRACERS = False         !   [Boolean] default = False</span>
<span id="L459">                                ! If true, use the NeverWorld2 tracers.</span>
<span id="L460"></span>
<span id="L461">! === module ideal_age_example ===</span>
<span id="L462">DO_IDEAL_AGE = True             !   [Boolean] default = True</span>
<span id="L463">                                ! If true, use an ideal age tracer that is set to 0 age in the boundary layer</span>
<span id="L464">                                ! and ages at unit rate in the interior.</span>
<span id="L465">DO_IDEAL_VINTAGE = False        !   [Boolean] default = False</span>
<span id="L466">                                ! If true, use an ideal vintage tracer that is set to an exponentially</span>
<span id="L467">                                ! increasing value in the boundary layer and is conserved thereafter.</span>
<span id="L468">DO_IDEAL_AGE_DATED = False      !   [Boolean] default = False</span>
<span id="L469">                                ! If true, use an ideal age tracer that is everywhere 0 before</span>
<span id="L470">                                ! IDEAL_AGE_DATED_START_YEAR, but the behaves like the standard ideal age tracer</span>
<span id="L471">                                ! - i.e. is set to 0 age in the boundary layer and ages at unit rate in the</span>
<span id="L472">                                ! interior.</span>
<span id="L473">DO_BL_RESIDENCE = False         !   [Boolean] default = False</span>
<span id="L474">                                ! If true, use a residence tracer that is set to 0 age in the interior and ages</span>
<span id="L475">                                ! at unit rate in the boundary layer.</span>
<span id="L476">USE_REAL_BL_DEPTH = False       !   [Boolean] default = False</span>
<span id="L477">                                ! If true, the ideal age tracers will use the boundary layer depth diagnosed</span>
<span id="L478">                                ! from the BL or bulkmixedlayer scheme.</span>
<span id="L479">AGE_IC_FILE = &quot;&quot;                ! default = &quot;&quot;</span>
<span id="L480">                                ! The file in which the age-tracer initial values can be found, or an empty</span>
<span id="L481">                                ! string for internal initialization.</span>
<span id="L482">AGE_IC_FILE_IS_Z = False        !   [Boolean] default = False</span>
<span id="L483">                                ! If true, AGE_IC_FILE is in depth space, not layer space</span>
<span id="L484">TRACERS_MAY_REINIT = False      !   [Boolean] default = False</span>
<span id="L485">                                ! If true, tracers may go through the initialization code if they are not found</span>
<span id="L486">                                ! in the restart files.  Otherwise it is a fatal error if the tracers are not</span>
<span id="L487">                                ! found in the restart files of a restarted run.</span>
<span id="L488"></span>
<span id="L489">! === module MOM_coord_initialization ===</span>
<span id="L490">COORD_CONFIG = &quot;file&quot;           ! default = &quot;none&quot;</span>
<span id="L491">                                ! This specifies how layers are to be defined:</span>
<span id="L492">                                !     ALE or none - used to avoid defining layers in ALE mode</span>
<span id="L493">                                !     file - read coordinate information from the file</span>
<span id="L494">                                !       specified by (COORD_FILE).</span>
<span id="L495">                                !     BFB - Custom coords for buoyancy-forced basin case</span>
<span id="L496">                                !       based on SST_S, T_BOT and DRHO_DT.</span>
<span id="L497">                                !     linear - linear based on interfaces not layers</span>
<span id="L498">                                !     layer_ref - linear based on layer densities</span>
<span id="L499">                                !     ts_ref - use reference temperature and salinity</span>
<span id="L500">                                !     ts_range - use range of temperature and salinity</span>
<span id="L501">                                !       (T_REF and S_REF) to determine surface density</span>
<span id="L502">                                !       and GINT calculate internal densities.</span>
<span id="L503">                                !     gprime - use reference density (RHO_0) for surface</span>
<span id="L504">                                !       density and GINT calculate internal densities.</span>
<span id="L505">                                !     ts_profile - use temperature and salinity profiles</span>
<span id="L506">                                !       (read from COORD_FILE) to set layer densities.</span>
<span id="L507">                                !     USER - call a user modified routine.</span>
<span id="L508">GFS = 9.8                       !   [m s-2] default = 9.8</span>
<span id="L509">                                ! The reduced gravity at the free surface.</span>
<span id="L510">COORD_FILE = &quot;Layer_coord50.nc&quot; !</span>
<span id="L511">                                ! The file from which the coordinate densities are read.</span>
<span id="L512">COORD_VAR = &quot;Layer&quot;             ! default = &quot;Layer&quot;</span>
<span id="L513">                                ! The variable in COORD_FILE that is to be used for the coordinate densities.</span>
<span id="L514">REGRIDDING_COORDINATE_MODE = &quot;HYCOM1&quot; ! default = &quot;LAYER&quot;</span>
<span id="L515">                                ! Coordinate mode for vertical regridding. Choose among the following</span>
<span id="L516">                                ! possibilities:  LAYER - Isopycnal or stacked shallow water layers</span>
<span id="L517">                                !  ZSTAR, Z* - stretched geopotential z*</span>
<span id="L518">                                !  SIGMA_SHELF_ZSTAR - stretched geopotential z* ignoring shelf</span>
<span id="L519">                                !  SIGMA - terrain following coordinates</span>
<span id="L520">                                !  RHO   - continuous isopycnal</span>
<span id="L521">                                !  HYCOM1 - HyCOM-like hybrid coordinate</span>
<span id="L522">                                !  HYBGEN - Hybrid coordinate from the Hycom hybgen code</span>
<span id="L523">                                !  ADAPTIVE - optimize for smooth neutral density surfaces</span>
<span id="L524">REGRIDDING_COORDINATE_UNITS = &quot;m&quot; ! default = &quot;m&quot;</span>
<span id="L525">                                ! Units of the regridding coordinate.</span>
<span id="L526">INTERPOLATION_SCHEME = &quot;P1M_H2&quot; ! default = &quot;P1M_H2&quot;</span>
<span id="L527">                                ! This sets the interpolation scheme to use to determine the new grid. These</span>
<span id="L528">                                ! parameters are only relevant when REGRIDDING_COORDINATE_MODE is set to a</span>
<span id="L529">                                ! function of state. Otherwise, it is not used. It can be one of the following</span>
<span id="L530">                                ! schemes:</span>
<span id="L531">                                !  P1M_H2     (2nd-order accurate)</span>
<span id="L532">                                !  P1M_H4     (2nd-order accurate)</span>
<span id="L533">                                !  P1M_IH4    (2nd-order accurate)</span>
<span id="L534">                                !  PLM        (2nd-order accurate)</span>
<span id="L535">                                !  PPM_CW     (3rd-order accurate)</span>
<span id="L536">                                !  PPM_H4     (3rd-order accurate)</span>
<span id="L537">                                !  PPM_IH4    (3rd-order accurate)</span>
<span id="L538">                                !  P3M_IH4IH3 (4th-order accurate)</span>
<span id="L539">                                !  P3M_IH6IH5 (4th-order accurate)</span>
<span id="L540">                                !  PQM_IH4IH3 (4th-order accurate)</span>
<span id="L541">                                !  PQM_IH6IH5 (5th-order accurate)</span>
<span id="L542">REMAPPING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L543">                                ! The vintage of the expressions and order of arithmetic to use for remapping.</span>
<span id="L544">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L545">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L546">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L547">REGRIDDING_ANSWER_DATE = 20181231 ! default = 99991231</span>
<span id="L548">                                ! The vintage of the expressions and order of arithmetic to use for regridding.</span>
<span id="L549">                                ! Values below 20190101 result in the use of older, less accurate expressions</span>
<span id="L550">                                ! that were in use at the end of 2018.  Higher values result in the use of more</span>
<span id="L551">                                ! robust and accurate forms of mathematically equivalent expressions.</span>
<span id="L552">BOUNDARY_EXTRAPOLATION = False  !   [Boolean] default = False</span>
<span id="L553">                                ! When defined, a proper high-order reconstruction scheme is used within</span>
<span id="L554">                                ! boundary cells rather than PCM. E.g., if PPM is used for remapping, a PPM</span>
<span id="L555">                                ! reconstruction will also be used within boundary cells.</span>
<span id="L556">ALE_COORDINATE_CONFIG = &quot;HYBRID:hycom1_50.nc,sigma2,dz&quot; ! default = &quot;UNIFORM&quot;</span>
<span id="L557">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L558">                                !  PARAM       - use the vector-parameter ALE_RESOLUTION</span>
<span id="L559">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L560">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L561">                                !                the filename and variable name, separated</span>
<span id="L562">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L563">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L564">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L565">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L566">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L567">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L568">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L569">                                !                the filename and two variable names, separated</span>
<span id="L570">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L571">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L572">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L573">                                !                the filename and two 3D variable names, separated</span>
<span id="L574">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L575">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L576">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L577">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L578">                                !                the filename and three variable names, separated</span>
<span id="L579">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L580">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L581">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L582">                                !                Map typically contains integer values, but it can</span>
<span id="L583">                                !                contain real values, I+w, which imply using</span>
<span id="L584">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L585">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L586">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L587">!ALE_RESOLUTION = 4*5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 17*30.0 !   [m]</span>
<span id="L588">                                ! The distribution of vertical resolution for the target</span>
<span id="L589">                                ! grid used for Eulerian-like coordinates. For example,</span>
<span id="L590">                                ! in z-coordinate mode, the parameter is a list of level</span>
<span id="L591">                                ! thicknesses (in m). In sigma-coordinate mode, the list</span>
<span id="L592">                                ! is of non-dimensional fractions of the water column.</span>
<span id="L593">!TARGET_DENSITIES = 1010.0, 1016.1289, 1020.843, 1024.821, 1027.0275, 1028.2911, 1029.2795, 1030.1194, 1030.8626, 1031.5364, 1032.1572, 1032.7358, 1033.2798, 1033.7948, 1034.2519, 1034.5828, 1034.8508, 1035.0821, 1035.2886, 1035.4769, 1035.6511, 1035.814, 1035.9675, 1036.1107, 1036.2411, 1036.3615, 1036.4739, 1036.5797, 1036.68, 1036.7755, 1036.8526, 1036.9024, 1036.9418, 1036.9754, 1037.0052, 1037.0323, 1037.0574, 1037.082, 1037.1066, 1037.1312, 1037.1558, 1037.1804, 1037.206, 1037.2337, 1037.2642, 1037.2986, 1037.3389, 1037.3901, 1037.475, 1037.7204, 1038.0 !   [kg m-3]</span>
<span id="L594">                                ! HYBRID target densities for interfaces</span>
<span id="L595">SHALLOW_ALE_RESOLUTION = 50*0.0 !   [m] default = 0.0</span>
<span id="L596">                                ! HYBGEN-style Z-sigma-Z near surface fixed coordinate. The default of all zeros</span>
<span id="L597">                                ! turns this option off. Let N_SIGMA be the number of consecutive non-zero</span>
<span id="L598">                                ! entries, typically &lt; NK. Use SHALLOW_ALE_RESOLUTION when rest depth is</span>
<span id="L599">                                ! shallower than SUM(SHALLOW_ALE_RESOLUTION(1:N_SIGMA)). Use ALE_RESOLUTION when</span>
<span id="L600">                                ! rest depth is deeper than SUM(ALE_RESOLUTION(1:N_SIGMA)). Otherwise use a</span>
<span id="L601">                                ! linear sum of the two weighted by rest depth.</span>
<span id="L602">REGRID_COMPRESSIBILITY_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L603">                                ! When interpolating potential density profiles we can add some artificial</span>
<span id="L604">                                ! compressibility solely to make homogeneous regions appear stratified.</span>
<span id="L605">MIN_THICKNESS = 0.001           !   [m] default = 0.001</span>
<span id="L606">                                ! When regridding, this is the minimum layer thickness allowed.</span>
<span id="L607">HYCOM1_ONLY_IMPROVES = False    !   [Boolean] default = False</span>
<span id="L608">                                ! When regridding, an interface is only moved if this improves the fit to the</span>
<span id="L609">                                ! target density.</span>
<span id="L610">MAXIMUM_INT_DEPTH_CONFIG = &quot;FNC1:5,12000,1.0,.125&quot; ! default = &quot;NONE&quot;</span>
<span id="L611">                                ! Determines how to specify the maximum interface depths.</span>
<span id="L612">                                ! Valid options are:</span>
<span id="L613">                                !  NONE        - there are no maximum interface depths</span>
<span id="L614">                                !  PARAM       - use the vector-parameter MAXIMUM_INTERFACE_DEPTHS</span>
<span id="L615">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L616">                                !                the filename and variable name, separated</span>
<span id="L617">                                !                by a comma or space, e.g. FILE:lev.nc,Z</span>
<span id="L618">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L619">!MAXIMUM_INT_DEPTHS = 0.0, 5.0, 19.625, 43.75, 77.5, 120.875, 173.875, 236.375, 308.5, 390.25, 481.625, 582.5, 693.0, 813.125, 942.875, 1082.125, 1231.0, 1389.5, 1557.5, 1735.125, 1922.375, 2119.25, 2325.625, 2541.625, 2767.25, 3002.5, 3247.25, 3501.625, 3765.625, 4039.25, 4322.375, 4615.125, 4917.5, 5229.5, 5551.0, 5882.125, 6222.875, 6573.125, 6933.0, 7302.5, 7681.625, 8070.25, 8468.5, 8876.375, 9293.875, 9720.875, 1.01575E+04, 1.060375E+04, 1.1059625E+04, 1.1525E+04, 1.2E+04 !   [m]</span>
<span id="L620">                                ! The list of maximum depths for each interface.</span>
<span id="L621">MAX_LAYER_THICKNESS_CONFIG = &quot;NONE&quot; ! default = &quot;NONE&quot;</span>
<span id="L622">                                ! Determines how to specify the maximum layer thicknesses.</span>
<span id="L623">                                ! Valid options are:</span>
<span id="L624">                                !  NONE        - there are no maximum layer thicknesses</span>
<span id="L625">                                !  PARAM       - use the vector-parameter MAX_LAYER_THICKNESS</span>
<span id="L626">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L627">                                !                the filename and variable name, separated</span>
<span id="L628">                                !                by a comma or space, e.g. FILE:lev.nc,Z</span>
<span id="L629">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L630">REMAPPING_SCHEME = &quot;PPM_H4&quot;     ! default = &quot;PLM&quot;</span>
<span id="L631">                                ! This sets the reconstruction scheme used for vertical remapping for all</span>
<span id="L632">                                ! variables. It can be one of the following schemes:</span>
<span id="L633">                                ! PCM         (1st-order accurate)</span>
<span id="L634">                                ! PLM         (2nd-order accurate)</span>
<span id="L635">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L636">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L637">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L638">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L639">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L640">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L641">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L642">VELOCITY_REMAPPING_SCHEME = &quot;PPM_H4&quot; ! default = &quot;PPM_H4&quot;</span>
<span id="L643">                                ! This sets the reconstruction scheme used for vertical remapping of velocities.</span>
<span id="L644">                                ! By default it is the same as REMAPPING_SCHEME. It can be one of the following</span>
<span id="L645">                                ! schemes:</span>
<span id="L646">                                ! PCM         (1st-order accurate)</span>
<span id="L647">                                ! PLM         (2nd-order accurate)</span>
<span id="L648">                                ! PLM_HYBGEN  (2nd-order accurate)</span>
<span id="L649">                                ! PPM_H4      (3rd-order accurate)</span>
<span id="L650">                                ! PPM_IH4     (3rd-order accurate)</span>
<span id="L651">                                ! PPM_HYBGEN  (3rd-order accurate)</span>
<span id="L652">                                ! WENO_HYBGEN (3rd-order accurate)</span>
<span id="L653">                                ! PQM_IH4IH3  (4th-order accurate)</span>
<span id="L654">                                ! PQM_IH6IH5  (5th-order accurate)</span>
<span id="L655">FATAL_CHECK_RECONSTRUCTIONS = False !   [Boolean] default = False</span>
<span id="L656">                                ! If true, cell-by-cell reconstructions are checked for consistency and if</span>
<span id="L657">                                ! non-monotonicity or an inconsistency is detected then a FATAL error is issued.</span>
<span id="L658">FATAL_CHECK_REMAPPING = False   !   [Boolean] default = False</span>
<span id="L659">                                ! If true, the results of remapping are checked for conservation and new extrema</span>
<span id="L660">                                ! and if an inconsistency is detected then a FATAL error is issued.</span>
<span id="L661">REMAP_BOUND_INTERMEDIATE_VALUES = False !   [Boolean] default = False</span>
<span id="L662">                                ! If true, the values on the intermediate grid used for remapping are forced to</span>
<span id="L663">                                ! be bounded, which might not be the case due to round off.</span>
<span id="L664">REMAP_BOUNDARY_EXTRAP = False   !   [Boolean] default = False</span>
<span id="L665">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L666">                                ! of piecewise constant</span>
<span id="L667">INIT_BOUNDARY_EXTRAP = False    !   [Boolean] default = False</span>
<span id="L668">                                ! If true, values at the interfaces of boundary cells are extrapolated instead</span>
<span id="L669">                                ! of piecewise constant during initialization.Defaults to REMAP_BOUNDARY_EXTRAP.</span>
<span id="L670">REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L671">                                ! This selects the remapping algorithm used in OM4 that does not use the full</span>
<span id="L672">                                ! reconstruction for the top- and lower-most sub-layers, but instead assumes</span>
<span id="L673">                                ! they are always vanished (untrue) and so just uses their edge values. We</span>
<span id="L674">                                ! recommend setting this option to false.</span>
<span id="L675">PARTIAL_CELL_VELOCITY_REMAP = False !   [Boolean] default = False</span>
<span id="L676">                                ! If true, use partial cell thicknesses at velocity points that are masked out</span>
<span id="L677">                                ! where they extend below the shallower of the neighboring bathymetry for</span>
<span id="L678">                                ! remapping velocity.</span>
<span id="L679">REMAP_AFTER_INITIALIZATION = False !   [Boolean] default = True</span>
<span id="L680">                                ! If true, applies regridding and remapping immediately after initialization so</span>
<span id="L681">                                ! that the state is ALE consistent. This is a legacy step and should not be</span>
<span id="L682">                                ! needed if the initialization is consistent with the coordinate mode.</span>
<span id="L683">REGRID_TIME_SCALE = 8.64E+04    !   [s] default = 0.0</span>
<span id="L684">                                ! The time-scale used in blending between the current (old) grid and the target</span>
<span id="L685">                                ! (new) grid. A short time-scale favors the target grid (0. or anything less</span>
<span id="L686">                                ! than DT_THERM) has no memory of the old grid. A very long time-scale makes the</span>
<span id="L687">                                ! model more Lagrangian.</span>
<span id="L688">REGRID_FILTER_SHALLOW_DEPTH = 0.0 !   [m] default = 0.0</span>
<span id="L689">                                ! The depth above which no time-filtering is applied. Above this depth final</span>
<span id="L690">                                ! grid exactly matches the target (new) grid.</span>
<span id="L691">REGRID_FILTER_DEEP_DEPTH = 0.0  !   [m] default = 0.0</span>
<span id="L692">                                ! The depth below which full time-filtering is applied with time-scale</span>
<span id="L693">                                ! REGRID_TIME_SCALE. Between depths REGRID_FILTER_SHALLOW_DEPTH and</span>
<span id="L694">                                ! REGRID_FILTER_SHALLOW_DEPTH the filter weights adopt a cubic profile.</span>
<span id="L695">REMAP_VEL_MASK_BBL_THICK = -0.001 !   [m] default = -0.001</span>
<span id="L696">                                ! A thickness of a bottom boundary layer below which velocities in thin layers</span>
<span id="L697">                                ! are zeroed out after remapping, following practice with Hybgen remapping, or a</span>
<span id="L698">                                ! negative value to avoid such filtering altogether.</span>
<span id="L699">REMAP_VEL_CONSERVE_KE = False   !   [Boolean] default = False</span>
<span id="L700">                                ! If true, a correction is applied to the baroclinic component of velocity after</span>
<span id="L701">                                ! remapping so that total KE is conserved. KE may not be conserved when</span>
<span id="L702">                                ! (CS%BBL_h_vel_mask &gt; 0.0) .and. (CS%h_vel_mask &gt; 0.0)</span>
<span id="L703"></span>
<span id="L704">! === module MOM_state_initialization ===</span>
<span id="L705">FATAL_INCONSISTENT_RESTART_TIME = False !   [Boolean] default = False</span>
<span id="L706">                                ! If true and a time_in value is provided to MOM_initialize_state, verify that</span>
<span id="L707">                                ! the time read from a restart file is the same as time_in, and issue a fatal</span>
<span id="L708">                                ! error if it is not.  Otherwise, simply set the time to time_in if present.</span>
<span id="L709">INIT_LAYERS_FROM_Z_FILE = True  !   [Boolean] default = False</span>
<span id="L710">                                ! If true, initialize the layer thicknesses, temperatures, and salinities from a</span>
<span id="L711">                                ! Z-space file on a latitude-longitude grid.</span>
<span id="L712"></span>
<span id="L713">! === module MOM_initialize_layers_from_Z ===</span>
<span id="L714">TEMP_SALT_Z_INIT_FILE = &quot;WOA05_pottemp_salt.nc&quot; ! default = &quot;temp_salt_z.nc&quot;</span>
<span id="L715">                                ! The name of the z-space input file used to initialize temperatures (T) and</span>
<span id="L716">                                ! salinities (S). If T and S are not in the same file, TEMP_Z_INIT_FILE and</span>
<span id="L717">                                ! SALT_Z_INIT_FILE must be set.</span>
<span id="L718">TEMP_Z_INIT_FILE = &quot;WOA05_pottemp_salt.nc&quot; ! default = &quot;WOA05_pottemp_salt.nc&quot;</span>
<span id="L719">                                ! The name of the z-space input file used to initialize temperatures, only.</span>
<span id="L720">SALT_Z_INIT_FILE = &quot;WOA05_pottemp_salt.nc&quot; ! default = &quot;WOA05_pottemp_salt.nc&quot;</span>
<span id="L721">                                ! The name of the z-space input file used to initialize temperatures, only.</span>
<span id="L722">Z_INIT_FILE_PTEMP_VAR = &quot;PTEMP&quot; ! default = &quot;ptemp&quot;</span>
<span id="L723">                                ! The name of the potential temperature variable in TEMP_Z_INIT_FILE.</span>
<span id="L724">Z_INIT_FILE_SALT_VAR = &quot;SALT&quot;   ! default = &quot;salt&quot;</span>
<span id="L725">                                ! The name of the salinity variable in SALT_Z_INIT_FILE.</span>
<span id="L726">Z_INIT_HOMOGENIZE = False       !   [Boolean] default = False</span>
<span id="L727">                                ! If True, then horizontally homogenize the interpolated initial conditions.</span>
<span id="L728">Z_INIT_ALE_REMAPPING = True     !   [Boolean] default = False</span>
<span id="L729">                                ! If True, then remap straight to model coordinate from file.</span>
<span id="L730">Z_INIT_REMAPPING_SCHEME = &quot;PPM_IH4&quot; ! default = &quot;PPM_IH4&quot;</span>
<span id="L731">                                ! The remapping scheme to use if using Z_INIT_ALE_REMAPPING is True.</span>
<span id="L732">Z_INIT_REMAP_GENERAL = True     !   [Boolean] default = False</span>
<span id="L733">                                ! If false, only initializes to z* coordinates. If true, allows initialization</span>
<span id="L734">                                ! directly to general coordinates.</span>
<span id="L735">Z_INIT_REMAP_FULL_COLUMN = True !   [Boolean] default = True</span>
<span id="L736">                                ! If false, only reconstructs profiles for valid data points. If true, inserts</span>
<span id="L737">                                ! vanished layers below the valid data.</span>
<span id="L738">Z_INIT_REMAP_OLD_ALG = False    !   [Boolean] default = False</span>
<span id="L739">                                ! If false, uses the preferred remapping algorithm for initialization. If true,</span>
<span id="L740">                                ! use an older, less robust algorithm for remapping.</span>
<span id="L741">TEMP_SALT_INIT_VERTICAL_REMAP_ONLY = False !   [Boolean] default = False</span>
<span id="L742">                                ! If true, initial conditions are on the model horizontal grid. Extrapolation</span>
<span id="L743">                                ! over missing ocean values is done using an ICE-9 procedure with vertical ALE</span>
<span id="L744">                                ! remapping .</span>
<span id="L745">Z_INIT_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L746">                                ! If true, use the OM4 remapping-via-subcells algorithm for initialization. See</span>
<span id="L747">                                ! REMAPPING_USE_OM4_SUBCELLS for more details. We recommend setting this option</span>
<span id="L748">                                ! to false.</span>
<span id="L749">HOR_REGRID_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L750">                                ! The vintage of the order of arithmetic for horizontal regridding.  Dates</span>
<span id="L751">                                ! before 20190101 give the same answers as the code did in late 2018, while</span>
<span id="L752">                                ! later versions add parentheses for rotational symmetry.  Dates after 20230101</span>
<span id="L753">                                ! use reproducing sums for global averages.</span>
<span id="L754">LAND_FILL_TEMP = 0.0            !   [degC] default = 0.0</span>
<span id="L755">                                ! A value to use to fill in ocean temperatures on land points.</span>
<span id="L756">LAND_FILL_SALIN = 35.0          !   [ppt] default = 35.0</span>
<span id="L757">                                ! A value to use to fill in ocean salinities on land points.</span>
<span id="L758">HORIZ_INTERP_TOL_TEMP = 0.001   !   [degC] default = 0.001</span>
<span id="L759">                                ! The tolerance in temperature changes between iterations when interpolating</span>
<span id="L760">                                ! from an input dataset using horiz_interp_and_extrap_tracer.  This routine</span>
<span id="L761">                                ! converges slowly, so an overly small tolerance can get expensive.</span>
<span id="L762">HORIZ_INTERP_TOL_SALIN = 0.001  !   [ppt] default = 0.001</span>
<span id="L763">                                ! The tolerance in salinity changes between iterations when interpolating from</span>
<span id="L764">                                ! an input dataset using horiz_interp_and_extrap_tracer.  This routine converges</span>
<span id="L765">                                ! slowly, so an overly small tolerance can get expensive.</span>
<span id="L766">DEPRESS_INITIAL_SURFACE = False !   [Boolean] default = False</span>
<span id="L767">                                ! If true,  depress the initial surface to avoid huge tsunamis when a large</span>
<span id="L768">                                ! surface pressure is applied.</span>
<span id="L769">TRIM_IC_FOR_P_SURF = False      !   [Boolean] default = False</span>
<span id="L770">                                ! If true, cuts way the top of the column for initial conditions at the depth</span>
<span id="L771">                                ! where the hydrostatic pressure matches the imposed surface pressure which is</span>
<span id="L772">                                ! read from file.</span>
<span id="L773">REGRID_ACCELERATE_INIT = False  !   [Boolean] default = False</span>
<span id="L774">                                ! If true, runs REGRID_ACCELERATE_ITERATIONS iterations of the regridding</span>
<span id="L775">                                ! algorithm to push the initial grid to be consistent with the initial</span>
<span id="L776">                                ! condition. Useful only for state-based and iterative coordinates.</span>
<span id="L777">VELOCITY_CONFIG = &quot;zero&quot;        ! default = &quot;zero&quot;</span>
<span id="L778">                                ! A string that determines how the initial velocities are specified for a new</span>
<span id="L779">                                ! run:</span>
<span id="L780">                                !     file - read velocities from the file specified</span>
<span id="L781">                                !       by (VELOCITY_FILE).</span>
<span id="L782">                                !     zero - the fluid is initially at rest.</span>
<span id="L783">                                !     uniform - the flow is uniform (determined by</span>
<span id="L784">                                !       parameters INITIAL_U_CONST and INITIAL_V_CONST).</span>
<span id="L785">                                !     rossby_front - a mixed layer front in thermal wind balance.</span>
<span id="L786">                                !     soliton - Equatorial Rossby soliton.</span>
<span id="L787">                                !     USER - call a user modified routine.</span>
<span id="L788">ODA_INCUPD = False              !   [Boolean] default = False</span>
<span id="L789">                                ! If true, oda incremental updates will be applied everywhere in the domain.</span>
<span id="L790">SPONGE = False                  !   [Boolean] default = False</span>
<span id="L791">                                ! If true, sponges may be applied anywhere in the domain. The exact location and</span>
<span id="L792">                                ! properties of those sponges are specified via SPONGE_CONFIG.</span>
<span id="L793"></span>
<span id="L794">! === module MOM_diag_mediator ===</span>
<span id="L795">NUM_DIAG_COORDS = 1             ! default = 1</span>
<span id="L796">                                ! The number of diagnostic vertical coordinates to use. For each coordinate, an</span>
<span id="L797">                                ! entry in DIAG_COORDS must be provided.</span>
<span id="L798">DIAG_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L799">                                ! If true, use the OM4 remapping-via-subcells algorithm for diagnostics. See</span>
<span id="L800">                                ! REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting this option to</span>
<span id="L801">                                ! false.</span>
<span id="L802">USE_INDEX_DIAGNOSTIC_AXES = False !   [Boolean] default = False</span>
<span id="L803">                                ! If true, use a grid index coordinate convention for diagnostic axes.</span>
<span id="L804">DIAG_COORDS = &quot;z Z ZSTAR&quot;       ! default = &quot;z Z ZSTAR&quot;</span>
<span id="L805">                                ! A list of string tuples associating diag_table modules to a coordinate</span>
<span id="L806">                                ! definition used for diagnostics. Each string is of the form &quot;MODULE_SUFFIX</span>
<span id="L807">                                ! PARAMETER_SUFFIX COORDINATE_NAME&quot;.</span>
<span id="L808">DIAG_MISVAL = 1.0E+20           !   [various] default = 1.0E+20</span>
<span id="L809">                                ! Set the default missing value to use for diagnostics.</span>
<span id="L810">DIAG_AS_CHKSUM = False          !   [Boolean] default = False</span>
<span id="L811">                                ! Instead of writing diagnostics to the diag manager, write a text file</span>
<span id="L812">                                ! containing the checksum (bitcount) of the array.</span>
<span id="L813">AVAILABLE_DIAGS_FILE = &quot;available_diags.000000&quot; ! default = &quot;available_diags.000000&quot;</span>
<span id="L814">                                ! A file into which to write a list of all available ocean diagnostics that can</span>
<span id="L815">                                ! be included in a diag_table.</span>
<span id="L816">DIAG_COORD_DEF_Z = &quot;WOA09&quot;      ! default = &quot;WOA09&quot;</span>
<span id="L817">                                ! Determines how to specify the coordinate resolution. Valid options are:</span>
<span id="L818">                                !  PARAM       - use the vector-parameter DIAG_COORD_RES_Z</span>
<span id="L819">                                !  UNIFORM[:N] - uniformly distributed</span>
<span id="L820">                                !  FILE:string - read from a file. The string specifies</span>
<span id="L821">                                !                the filename and variable name, separated</span>
<span id="L822">                                !                by a comma or space, e.g. FILE:lev.nc,dz</span>
<span id="L823">                                !                or FILE:lev.nc,interfaces=zw</span>
<span id="L824">                                !  WOA09[:N]   - the WOA09 vertical grid (approximately)</span>
<span id="L825">                                !  WOA09INT[:N] - layers spanned by the WOA09 depths</span>
<span id="L826">                                !  WOA23INT[:N] - layers spanned by the WOA23 depths</span>
<span id="L827">                                !  FNC1:string - FNC1:dz_min,H_total,power,precision</span>
<span id="L828">                                !  HYBRID:string - read from a file. The string specifies</span>
<span id="L829">                                !                the filename and two variable names, separated</span>
<span id="L830">                                !                by a comma or space, for sigma-2 and dz.</span>
<span id="L831">                                !                e.g. HYBRID:vgrid.nc,sigma2,dz</span>
<span id="L832">                                !  HYBRID_3D:string - read from a file. The string specifies</span>
<span id="L833">                                !                the filename and two 3D variable names, separated</span>
<span id="L834">                                !                by a comma or space, for sigma-2 and dz. The</span>
<span id="L835">                                !                latter can be FNC1:string which is used everywhere.</span>
<span id="L836">                                !                e.g. HYBRID_3D:vgrid.nc,sigma2,dz</span>
<span id="L837">                                !  HYBRID_MAP:string - read from a file. The string specifies</span>
<span id="L838">                                !                the filename and three variable names, separated</span>
<span id="L839">                                !                by a comma or space, for map, sigma-2 and dz.</span>
<span id="L840">                                !                Map is a spatial index array with, maxval(map)=N,</span>
<span id="L841">                                !                and the others are 2D arrays containing N profiles.</span>
<span id="L842">                                !                Map typically contains integer values, but it can</span>
<span id="L843">                                !                contain real values, I+w, which imply using</span>
<span id="L844">                                !                the weighted sum of profiles I and I+1.</span>
<span id="L845">                                !                Dz can be FNC1:string which is used everywhere.</span>
<span id="L846">                                !                e.g. HYBRID_MAP:vgrid.nc,map,sigma2,dz</span>
<span id="L847"></span>
<span id="L848">! === module MOM_MEKE ===</span>
<span id="L849">USE_MEKE = True                 !   [Boolean] default = False</span>
<span id="L850">                                ! If true, turns on the MEKE scheme which calculates a sub-grid mesoscale eddy</span>
<span id="L851">                                ! kinetic energy budget.</span>
<span id="L852">MEKE_IN_DYNAMICS = True         !   [Boolean] default = True</span>
<span id="L853">                                ! If true, step MEKE forward with the dynamicsotherwise with the tracer</span>
<span id="L854">                                ! timestep.</span>
<span id="L855">EKE_SOURCE = &quot;prog&quot;             ! default = &quot;prog&quot;</span>
<span id="L856">                                ! Determine the where EKE comes from:</span>
<span id="L857">                                !   &#x27;prog&#x27;: Calculated solving EKE equation</span>
<span id="L858">                                !   &#x27;file&#x27;: Read in from a file</span>
<span id="L859">                                !   &#x27;dbclient&#x27;: Retrieved from ML-database</span>
<span id="L860">MEKE_DAMPING = 0.0              !   [s-1] default = 0.0</span>
<span id="L861">                                ! The local depth-independent MEKE dissipation rate.</span>
<span id="L862">MEKE_CD_SCALE = 0.0             !   [nondim] default = 0.0</span>
<span id="L863">                                ! The ratio of the bottom eddy velocity to the column mean eddy velocity, i.e.</span>
<span id="L864">                                ! sqrt(2*MEKE). This should be less than 1 to account for the surface</span>
<span id="L865">                                ! intensification of MEKE.</span>
<span id="L866">MEKE_CB = 25.0                  !   [nondim] default = 25.0</span>
<span id="L867">                                ! A coefficient in the expression for the ratio of bottom projected eddy energy</span>
<span id="L868">                                ! and mean column energy (see Jansen et al. 2015).</span>
<span id="L869">MEKE_MIN_GAMMA2 = 1.0E-04       !   [nondim] default = 1.0E-04</span>
<span id="L870">                                ! The minimum allowed value of gamma_b^2.</span>
<span id="L871">MEKE_CT = 50.0                  !   [nondim] default = 50.0</span>
<span id="L872">                                ! A coefficient in the expression for the ratio of barotropic eddy energy and</span>
<span id="L873">                                ! mean column energy (see Jansen et al. 2015).</span>
<span id="L874">MEKE_GMCOEFF = 1.0              !   [nondim] default = -1.0</span>
<span id="L875">                                ! The efficiency of the conversion of potential energy into MEKE by the</span>
<span id="L876">                                ! thickness mixing parameterization. If MEKE_GMCOEFF is negative, this</span>
<span id="L877">                                ! conversion is not used or calculated.</span>
<span id="L878">MEKE_GEOMETRIC = False          !   [Boolean] default = False</span>
<span id="L879">                                ! If MEKE_GEOMETRIC is true, uses the GM coefficient formulation from the</span>
<span id="L880">                                ! GEOMETRIC framework (Marshall et al., 2012).</span>
<span id="L881">MEKE_GEOMETRIC_ALPHA = 0.05     !   [nondim] default = 0.05</span>
<span id="L882">                                ! The nondimensional coefficient governing the efficiency of the GEOMETRIC</span>
<span id="L883">                                ! thickness diffusion.</span>
<span id="L884">MEKE_EQUILIBRIUM_ALT = False    !   [Boolean] default = False</span>
<span id="L885">                                ! If true, use an alternative formula for computing the (equilibrium)initial</span>
<span id="L886">                                ! value of MEKE.</span>
<span id="L887">MEKE_EQUILIBRIUM_RESTORING = False !   [Boolean] default = False</span>
<span id="L888">                                ! If true, restore MEKE back to its equilibrium value, which is calculated at</span>
<span id="L889">                                ! each time step.</span>
<span id="L890">MEKE_FRCOEFF = -1.0             !   [nondim] default = -1.0</span>
<span id="L891">                                ! The efficiency of the conversion of mean energy into MEKE.  If MEKE_FRCOEFF is</span>
<span id="L892">                                ! negative, this conversion is not used or calculated.</span>
<span id="L893">MEKE_BHFRCOEFF = -1.0           !   [nondim] default = -1.0</span>
<span id="L894">                                ! The efficiency of the conversion of mean energy into MEKE by the biharmonic</span>
<span id="L895">                                ! dissipation.  If MEKE_bhFRCOEFF is negative, this conversion is not used or</span>
<span id="L896">                                ! calculated.</span>
<span id="L897">MEKE_GMECOEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L898">                                ! The efficiency of the conversion of MEKE into mean energy by GME.  If</span>
<span id="L899">                                ! MEKE_GMECOEFF is negative, this conversion is not used or calculated.</span>
<span id="L900">MEKE_BGSRC = 0.0                !   [W kg-1] default = 0.0</span>
<span id="L901">                                ! A background energy source for MEKE.</span>
<span id="L902">MEKE_KH = -1.0                  !   [m2 s-1] default = -1.0</span>
<span id="L903">                                ! A background lateral diffusivity of MEKE. Use a negative value to not apply</span>
<span id="L904">                                ! lateral diffusion to MEKE.</span>
<span id="L905">MEKE_K4 = -1.0                  !   [m4 s-1] default = -1.0</span>
<span id="L906">                                ! A lateral bi-harmonic diffusivity of MEKE. Use a negative value to not apply</span>
<span id="L907">                                ! bi-harmonic diffusion to MEKE.</span>
<span id="L908">MEKE_DTSCALE = 1.0              !   [nondim] default = 1.0</span>
<span id="L909">                                ! A scaling factor to accelerate the time evolution of MEKE.</span>
<span id="L910">MEKE_POSITIVE = False           !   [Boolean] default = False</span>
<span id="L911">                                ! If true, it guarantees that MEKE will always be &gt;= 0.</span>
<span id="L912">MEKE_KHCOEFF = 1.0              !   [nondim] default = 1.0</span>
<span id="L913">                                ! A scaling factor in the expression for eddy diffusivity which is otherwise</span>
<span id="L914">                                ! proportional to the MEKE velocity- scale times an eddy mixing-length. This</span>
<span id="L915">                                ! factor must be &gt;0 for MEKE to contribute to the thickness/ and tracer</span>
<span id="L916">                                ! diffusivity in the rest of the model.</span>
<span id="L917">MEKE_USCALE = 0.0               !   [m s-1] default = 0.0</span>
<span id="L918">                                ! The background velocity that is combined with MEKE to calculate the bottom</span>
<span id="L919">                                ! drag.</span>
<span id="L920">MEKE_GM_SRC_ALT = False         !   [Boolean] default = False</span>
<span id="L921">                                ! If true, use the GM energy conversion form S^2*N^2*kappa rather than the</span>
<span id="L922">                                ! streamfunction for the MEKE GM source term.</span>
<span id="L923">MEKE_VISC_DRAG = True           !   [Boolean] default = True</span>
<span id="L924">                                ! If true, use the vertvisc_type to calculate the bottom drag acting on MEKE.</span>
<span id="L925">MEKE_KHTH_FAC = 0.0             !   [nondim] default = 0.0</span>
<span id="L926">                                ! A factor that maps MEKE%Kh to KhTh.</span>
<span id="L927">MEKE_KHTR_FAC = 0.0             !   [nondim] default = 0.0</span>
<span id="L928">                                ! A factor that maps MEKE%Kh to KhTr.</span>
<span id="L929">MEKE_KHMEKE_FAC = 0.0           !   [nondim] default = 0.0</span>
<span id="L930">                                ! A factor that maps MEKE%Kh to Kh for MEKE itself.</span>
<span id="L931">MEKE_OLD_LSCALE = False         !   [Boolean] default = False</span>
<span id="L932">                                ! If true, use the old formula for length scale which is a function of grid</span>
<span id="L933">                                ! spacing and deformation radius.</span>
<span id="L934">MEKE_MIN_LSCALE = False         !   [Boolean] default = False</span>
<span id="L935">                                ! If true, use a strict minimum of provided length scales rather than harmonic</span>
<span id="L936">                                ! mean.</span>
<span id="L937">MEKE_RD_MAX_SCALE = False       !   [Boolean] default = False</span>
<span id="L938">                                ! If true, the length scale used by MEKE is the minimum of the deformation</span>
<span id="L939">                                ! radius or grid-spacing. Only used if MEKE_OLD_LSCALE=True</span>
<span id="L940">MEKE_VISCOSITY_COEFF_KU = 0.0   !   [nondim] default = 0.0</span>
<span id="L941">                                ! If non-zero, is the scaling coefficient in the expression forviscosity used to</span>
<span id="L942">                                ! parameterize harmonic lateral momentum mixing byunresolved eddies represented</span>
<span id="L943">                                ! by MEKE. Can be negative torepresent backscatter from the unresolved eddies.</span>
<span id="L944">MEKE_VISCOSITY_COEFF_AU = 0.0   !   [nondim] default = 0.0</span>
<span id="L945">                                ! If non-zero, is the scaling coefficient in the expression forviscosity used to</span>
<span id="L946">                                ! parameterize biharmonic lateral momentum mixing byunresolved eddies</span>
<span id="L947">                                ! represented by MEKE. Can be negative torepresent backscatter from the</span>
<span id="L948">                                ! unresolved eddies.</span>
<span id="L949">MEKE_FIXED_MIXING_LENGTH = 0.0  !   [m] default = 0.0</span>
<span id="L950">                                ! If positive, is a fixed length contribution to the expression for mixing</span>
<span id="L951">                                ! length used in MEKE-derived diffusivity.</span>
<span id="L952">MEKE_FIXED_TOTAL_DEPTH = True   !   [Boolean] default = True</span>
<span id="L953">                                ! If true, use the nominal bathymetric depth as the estimate of the time-varying</span>
<span id="L954">                                ! ocean depth.  Otherwise base the depth on the total ocean massper unit area.</span>
<span id="L955">MEKE_ALPHA_DEFORM = 0.0         !   [nondim] default = 0.0</span>
<span id="L956">                                ! If positive, is a coefficient weighting the deformation scale in the</span>
<span id="L957">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L958">MEKE_ALPHA_RHINES = 0.0         !   [nondim] default = 0.0</span>
<span id="L959">                                ! If positive, is a coefficient weighting the Rhines scale in the expression for</span>
<span id="L960">                                ! mixing length used in MEKE-derived diffusivity.</span>
<span id="L961">MEKE_ALPHA_EADY = 0.0           !   [nondim] default = 0.0</span>
<span id="L962">                                ! If positive, is a coefficient weighting the Eady length scale in the</span>
<span id="L963">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L964">MEKE_ALPHA_FRICT = 0.0          !   [nondim] default = 0.0</span>
<span id="L965">                                ! If positive, is a coefficient weighting the frictional arrest scale in the</span>
<span id="L966">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L967">MEKE_ALPHA_GRID = 0.0           !   [nondim] default = 0.0</span>
<span id="L968">                                ! If positive, is a coefficient weighting the grid-spacing as a scale in the</span>
<span id="L969">                                ! expression for mixing length used in MEKE-derived diffusivity.</span>
<span id="L970">MEKE_COLD_START = False         !   [Boolean] default = False</span>
<span id="L971">                                ! If true, initialize EKE to zero. Otherwise a local equilibrium solution is</span>
<span id="L972">                                ! used as an initial condition for EKE.</span>
<span id="L973">MEKE_BACKSCAT_RO_C = 0.0        !   [nondim] default = 0.0</span>
<span id="L974">                                ! The coefficient in the Rossby number function for scaling the biharmonic</span>
<span id="L975">                                ! frictional energy source. Setting to non-zero enables the Rossby number</span>
<span id="L976">                                ! function.</span>
<span id="L977">MEKE_BACKSCAT_RO_POW = 0.0      !   [nondim] default = 0.0</span>
<span id="L978">                                ! The power in the Rossby number function for scaling the biharmonic frictional</span>
<span id="L979">                                ! energy source.</span>
<span id="L980">MEKE_ADVECTION_FACTOR = 0.0     !   [nondim] default = 0.0</span>
<span id="L981">                                ! A scale factor in front of advection of eddy energy. Zero turns advection off.</span>
<span id="L982">                                ! Using unity would be normal but other values could accommodate a mismatch</span>
<span id="L983">                                ! between the advecting barotropic flow and the vertical structure of MEKE.</span>
<span id="L984">MEKE_TOPOGRAPHIC_BETA = 0.0     !   [nondim] default = 0.0</span>
<span id="L985">                                ! A scale factor to determine how much topographic beta is weighed in computing</span>
<span id="L986">                                ! beta in the expression of Rhines scale. Use 1 if full topographic beta effect</span>
<span id="L987">                                ! is considered; use 0 if it&#x27;s completely ignored.</span>
<span id="L988">SQG_USE_MEKE = False            !   [Boolean] default = False</span>
<span id="L989">                                ! If true, the eddy scale of MEKE is used for the SQG vertical structure</span>
<span id="L990">CDRAG = 0.003                   !   [nondim] default = 0.003</span>
<span id="L991">                                ! CDRAG is the drag coefficient relating the magnitude of the velocity field to</span>
<span id="L992">                                ! the bottom stress.</span>
<span id="L993">MEKE_CDRAG = 0.003              !   [nondim] default = 0.003</span>
<span id="L994">                                ! Drag coefficient relating the magnitude of the velocity field to the bottom</span>
<span id="L995">                                ! stress in MEKE.</span>
<span id="L996"></span>
<span id="L997">! === module MOM_lateral_mixing_coeffs ===</span>
<span id="L998">USE_VARIABLE_MIXING = True      !   [Boolean] default = False</span>
<span id="L999">                                ! If true, the variable mixing code will be called.  This allows diagnostics to</span>
<span id="L1000">                                ! be created even if the scheme is not used.  If KHTR_SLOPE_CFF&gt;0 or</span>
<span id="L1001">                                ! KhTh_Slope_Cff&gt;0, this is set to true regardless of what is in the parameter</span>
<span id="L1002">                                ! file.</span>
<span id="L1003">USE_VISBECK = False             !   [Boolean] default = False</span>
<span id="L1004">                                ! If true, use the Visbeck et al. (1997) formulation for</span>
<span id="L1005">                                ! thickness diffusivity.</span>
<span id="L1006">RESOLN_SCALED_KH = True         !   [Boolean] default = False</span>
<span id="L1007">                                ! If true, the Laplacian lateral viscosity is scaled away when the first</span>
<span id="L1008">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L1009">DEPTH_SCALED_KHTH = False       !   [Boolean] default = False</span>
<span id="L1010">                                ! If true, KHTH is scaled away when the depth is shallowerthan a reference</span>
<span id="L1011">                                ! depth: KHTH = MIN(1,H/H0)**N * KHTH, where H0 is a reference depth, controlled</span>
<span id="L1012">                                ! via DEPTH_SCALED_KHTH_H0, and the exponent (N) is controlled via</span>
<span id="L1013">                                ! DEPTH_SCALED_KHTH_EXP.</span>
<span id="L1014">RESOLN_SCALED_KHTH = True       !   [Boolean] default = False</span>
<span id="L1015">                                ! If true, the interface depth diffusivity is scaled away when the first</span>
<span id="L1016">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L1017">RESOLN_SCALED_KHTR = False      !   [Boolean] default = False</span>
<span id="L1018">                                ! If true, the epipycnal tracer diffusivity is scaled away when the first</span>
<span id="L1019">                                ! baroclinic deformation radius is well resolved.</span>
<span id="L1020">RESOLN_USE_EBT = False          !   [Boolean] default = False</span>
<span id="L1021">                                ! If true, uses the equivalent barotropic wave speed instead of first baroclinic</span>
<span id="L1022">                                ! wave for calculating the resolution fn.</span>
<span id="L1023">BACKSCAT_EBT_POWER = 0.0        !   [nondim] default = 0.0</span>
<span id="L1024">                                ! Power to raise EBT vertical structure to when backscatter has vertical</span>
<span id="L1025">                                ! structure.</span>
<span id="L1026">BS_USE_SQG_STRUCT = False       !   [Boolean] default = False</span>
<span id="L1027">                                ! If true, the SQG vertical structure is used for backscatter on the condition</span>
<span id="L1028">                                ! that BS_EBT_power=0</span>
<span id="L1029">KHTH_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1030">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1031">                                ! thickness diffusivity.</span>
<span id="L1032">KHTH_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1033">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L1034">                                ! of thickness diffusivity.</span>
<span id="L1035">KHTR_USE_EBT_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1036">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1037">                                ! tracer diffusivity.</span>
<span id="L1038">KHTR_USE_SQG_STRUCT = False     !   [Boolean] default = False</span>
<span id="L1039">                                ! If true, uses the surface quasigeostrophic structure as the vertical structure</span>
<span id="L1040">                                ! of tracer diffusivity.</span>
<span id="L1041">KD_GL90_USE_EBT_STRUCT = False  !   [Boolean] default = False</span>
<span id="L1042">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1043">                                ! diffusivity in the GL90 scheme.</span>
<span id="L1044">KD_GL90_USE_SQG_STRUCT = False  !   [Boolean] default = False</span>
<span id="L1045">                                ! If true, uses the equivalent barotropic structure as the vertical structure of</span>
<span id="L1046">                                ! diffusivity in the GL90 scheme.</span>
<span id="L1047">KHTH_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L1048">                                ! The nondimensional coefficient in the Visbeck formula for the interface depth</span>
<span id="L1049">                                ! diffusivity</span>
<span id="L1050">KHTR_SLOPE_CFF = 0.0            !   [nondim] default = 0.0</span>
<span id="L1051">                                ! The nondimensional coefficient in the Visbeck formula for the epipycnal tracer</span>
<span id="L1052">                                ! diffusivity</span>
<span id="L1053">USE_STORED_SLOPES = True        !   [Boolean] default = False</span>
<span id="L1054">                                ! If true, the isopycnal slopes are calculated once and stored for re-use. This</span>
<span id="L1055">                                ! uses more memory but avoids calling the equation of state more times than</span>
<span id="L1056">                                ! should be necessary.</span>
<span id="L1057">VERY_SMALL_FREQUENCY = 1.0E-17  !   [s-1] default = 1.0E-17</span>
<span id="L1058">                                ! A miniscule frequency that is used to avoid division by 0.  The default value</span>
<span id="L1059">                                ! is roughly (pi / (the age of the universe)).</span>
<span id="L1060">USE_STANLEY_ISO = False         !   [Boolean] default = False</span>
<span id="L1061">                                ! If true, turn on Stanley SGS T variance parameterization in isopycnal slope</span>
<span id="L1062">                                ! code.</span>
<span id="L1063">KD_SMOOTH = 1.0E-06             !   [m2 s-1] default = 1.0E-06</span>
<span id="L1064">                                ! A diapycnal diffusivity that is used to interpolate more sensible values of T</span>
<span id="L1065">                                ! &amp; S into thin layers.</span>
<span id="L1066">USE_SIMPLER_EADY_GROWTH_RATE = False !   [Boolean] default = False</span>
<span id="L1067">                                ! If true, use a simpler method to calculate the Eady growth rate that avoids</span>
<span id="L1068">                                ! division by layer thickness. Recommended.</span>
<span id="L1069">VARMIX_KTOP = 2                 !   [nondim] default = 2</span>
<span id="L1070">                                ! The layer number at which to start vertical integration of S*N for purposes of</span>
<span id="L1071">                                ! finding the Eady growth rate.</span>
<span id="L1072">KH_RES_SCALE_COEF = 1.0         !   [nondim] default = 1.0</span>
<span id="L1073">                                ! A coefficient that determines how KhTh is scaled away if RESOLN_SCALED_... is</span>
<span id="L1074">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER).</span>
<span id="L1075">KH_RES_FN_POWER = 2             ! default = 2</span>
<span id="L1076">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L1077">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L1078">                                ! greater than 100 results in a step-function being used.</span>
<span id="L1079">VISC_RES_SCALE_COEF = 1.0       !   [nondim] default = 1.0</span>
<span id="L1080">                                ! A coefficient that determines how Kh is scaled away if RESOLN_SCALED_... is</span>
<span id="L1081">                                ! true, as F = 1 / (1 + (KH_RES_SCALE_COEF*Rd/dx)^KH_RES_FN_POWER). This</span>
<span id="L1082">                                ! function affects lateral viscosity, Kh, and not KhTh.</span>
<span id="L1083">VISC_RES_FN_POWER = 2           ! default = 2</span>
<span id="L1084">                                ! The power of dx/Ld in the Kh resolution function.  Any positive integer may be</span>
<span id="L1085">                                ! used, although even integers are more efficient to calculate.  Setting this</span>
<span id="L1086">                                ! greater than 100 results in a step-function being used. This function affects</span>
<span id="L1087">                                ! lateral viscosity, Kh, and not KhTh.</span>
<span id="L1088">INTERPOLATE_RES_FN = False      !   [Boolean] default = False</span>
<span id="L1089">                                ! If true, interpolate the resolution function to the velocity points from the</span>
<span id="L1090">                                ! thickness points; otherwise interpolate the wave speed and calculate the</span>
<span id="L1091">                                ! resolution function independently at each point.</span>
<span id="L1092">GILL_EQUATORIAL_LD = True       !   [Boolean] default = True</span>
<span id="L1093">                                ! If true, uses Gill&#x27;s definition of the baroclinic equatorial deformation</span>
<span id="L1094">                                ! radius, otherwise, if false, use Pedlosky&#x27;s definition. These definitions</span>
<span id="L1095">                                ! differ by a factor of 2 in front of the beta term in the denominator. Gill&#x27;s</span>
<span id="L1096">                                ! is the more appropriate definition.</span>
<span id="L1097">INTERNAL_WAVE_SPEED_TOL = 0.001 !   [nondim] default = 0.001</span>
<span id="L1098">                                ! The fractional tolerance for finding the wave speeds.</span>
<span id="L1099">INTERNAL_WAVE_SPEED_MIN = 0.0   !   [m s-1] default = 0.0</span>
<span id="L1100">                                ! A floor in the first mode speed below which 0 used instead.</span>
<span id="L1101">INTERNAL_WAVE_SPEED_BETTER_EST = False !   [Boolean] default = True</span>
<span id="L1102">                                ! If true, use a more robust estimate of the first mode wave speed as the</span>
<span id="L1103">                                ! starting point for iterations.</span>
<span id="L1104">EBT_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1105">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1106">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1107">                                ! this option to false.</span>
<span id="L1108">USE_QG_LEITH_GM = False         !   [Boolean] default = False</span>
<span id="L1109">                                ! If true, use the QG Leith viscosity as the GM coefficient.</span>
<span id="L1110"></span>
<span id="L1111">! === module MOM_set_visc ===</span>
<span id="L1112">SET_VISC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1113">                                ! The vintage of the order of arithmetic and expressions in the set viscosity</span>
<span id="L1114">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1115">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1116">BOTTOMDRAGLAW = True            !   [Boolean] default = True</span>
<span id="L1117">                                ! If true, the bottom stress is calculated with a drag law of the form</span>
<span id="L1118">                                ! c_drag*|u|*u. The velocity magnitude may be an assumed value or it may be</span>
<span id="L1119">                                ! based on the actual velocity in the bottommost HBBL, depending on LINEAR_DRAG.</span>
<span id="L1120">DRAG_AS_BODY_FORCE = False      !   [Boolean] default = False</span>
<span id="L1121">                                ! If true, the bottom stress is imposed as an explicit body force applied over a</span>
<span id="L1122">                                ! fixed distance from the bottom, rather than as an implicit calculation based</span>
<span id="L1123">                                ! on an enhanced near-bottom viscosity. The thickness of the bottom boundary</span>
<span id="L1124">                                ! layer is HBBL.</span>
<span id="L1125">CHANNEL_DRAG = True             !   [Boolean] default = False</span>
<span id="L1126">                                ! If true, the bottom drag is exerted directly on each layer proportional to the</span>
<span id="L1127">                                ! fraction of the bottom it overlies.</span>
<span id="L1128">LINEAR_DRAG = False             !   [Boolean] default = False</span>
<span id="L1129">                                ! If LINEAR_DRAG and BOTTOMDRAGLAW are defined the drag law is</span>
<span id="L1130">                                ! cdrag*DRAG_BG_VEL*u.</span>
<span id="L1131">DYNAMIC_VISCOUS_ML = False      !   [Boolean] default = False</span>
<span id="L1132">                                ! If true, use a bulk Richardson number criterion to determine the mixed layer</span>
<span id="L1133">                                ! thickness for viscosity.</span>
<span id="L1134">HBBL = 10.0                     !   [m]</span>
<span id="L1135">                                ! The thickness of a bottom boundary layer with a viscosity increased by</span>
<span id="L1136">                                ! KV_EXTRA_BBL if BOTTOMDRAGLAW is not defined, or the thickness over which</span>
<span id="L1137">                                ! near-bottom velocities are averaged for the drag law if BOTTOMDRAGLAW is</span>
<span id="L1138">                                ! defined but LINEAR_DRAG is not.</span>
<span id="L1139">BBL_USE_TIDAL_BG = False        !   [Boolean] default = False</span>
<span id="L1140">                                ! Flag to use the tidal RMS amplitude in place of constant background velocity</span>
<span id="L1141">                                ! for computing u* in the BBL. This flag is only used when BOTTOMDRAGLAW is true</span>
<span id="L1142">                                ! and LINEAR_DRAG is false.</span>
<span id="L1143">DRAG_BG_VEL = 0.1               !   [m s-1] default = 0.0</span>
<span id="L1144">                                ! DRAG_BG_VEL is either the assumed bottom velocity (with LINEAR_DRAG) or an</span>
<span id="L1145">                                ! unresolved  velocity that is combined with the resolved velocity to estimate</span>
<span id="L1146">                                ! the velocity magnitude.  DRAG_BG_VEL is only used when BOTTOMDRAGLAW is</span>
<span id="L1147">                                ! defined.</span>
<span id="L1148">BBL_USE_EOS = True              !   [Boolean] default = True</span>
<span id="L1149">                                ! If true, use the equation of state in determining the properties of the bottom</span>
<span id="L1150">                                ! boundary layer.  Otherwise use the layer target potential densities.  The</span>
<span id="L1151">                                ! default of this parameter is the value of USE_EOS.</span>
<span id="L1152">BBL_THICK_MIN = 0.1             !   [m] default = 0.0</span>
<span id="L1153">                                ! The minimum bottom boundary layer thickness that can be used with</span>
<span id="L1154">                                ! BOTTOMDRAGLAW. This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum</span>
<span id="L1155">                                ! near-bottom viscosity.</span>
<span id="L1156">HTBL_SHELF_MIN = 0.1            !   [m] default = 0.1</span>
<span id="L1157">                                ! The minimum top boundary layer thickness that can be used with BOTTOMDRAGLAW.</span>
<span id="L1158">                                ! This might be Kv/(cdrag*drag_bg_vel) to give Kv as the minimum near-top</span>
<span id="L1159">                                ! viscosity.</span>
<span id="L1160">HTBL_SHELF = 10.0               !   [m] default = 10.0</span>
<span id="L1161">                                ! The thickness over which near-surface velocities are averaged for the drag law</span>
<span id="L1162">                                ! under an ice shelf.  By default this is the same as HBBL</span>
<span id="L1163">KV = 1.0E-04                    !   [m2 s-1]</span>
<span id="L1164">                                ! The background kinematic viscosity in the interior. The molecular value, ~1e-6</span>
<span id="L1165">                                ! m2 s-1, may be used.</span>
<span id="L1166">KV_BBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L1167">                                ! The minimum viscosities in the bottom boundary layer.</span>
<span id="L1168">KV_TBL_MIN = 1.0E-04            !   [m2 s-1] default = 1.0E-04</span>
<span id="L1169">                                ! The minimum viscosities in the top boundary layer.</span>
<span id="L1170">CORRECT_BBL_BOUNDS = False      !   [Boolean] default = False</span>
<span id="L1171">                                ! If true, uses the correct bounds on the BBL thickness and viscosity so that</span>
<span id="L1172">                                ! the bottom layer feels the intended drag.</span>
<span id="L1173">SMAG_CONST_CHANNEL = 0.15       !   [nondim] default = 0.15</span>
<span id="L1174">                                ! The nondimensional Laplacian Smagorinsky constant used in calculating the</span>
<span id="L1175">                                ! channel drag if it is enabled.  The default is to use the same value as</span>
<span id="L1176">                                ! SMAG_LAP_CONST if it is defined, or 0.15 if it is not. The value used is also</span>
<span id="L1177">                                ! 0.15 if the specified value is negative.</span>
<span id="L1178">TRIG_CHANNEL_DRAG_WIDTHS = True !   [Boolean] default = True</span>
<span id="L1179">                                ! If true, use trigonometric expressions to determine the fractional open</span>
<span id="L1180">                                ! interface lengths for concave topography.</span>
<span id="L1181">CHANNEL_DRAG_MAX_BBL_THICK = 5.0 !   [m] default = 5.0</span>
<span id="L1182">                                ! The maximum bottom boundary layer thickness over which the channel drag is</span>
<span id="L1183">                                ! exerted, or a negative value for no fixed limit, instead basing the BBL</span>
<span id="L1184">                                ! thickness on the bottom stress, rotation and stratification.  The default is</span>
<span id="L1185">                                ! proportional to HBBL if USE_JACKSON_PARAM or DRAG_AS_BODY_FORCE is true.</span>
<span id="L1186"></span>
<span id="L1187">! === module MOM_thickness_diffuse ===</span>
<span id="L1188">KHTH = 600.0                    !   [m2 s-1] default = 0.0</span>
<span id="L1189">                                ! The background horizontal thickness diffusivity.</span>
<span id="L1190">READ_KHTH = False               !   [Boolean] default = False</span>
<span id="L1191">                                ! If true, read a file (given by KHTH_FILE) containing the spatially varying</span>
<span id="L1192">                                ! horizontal isopycnal height diffusivity.</span>
<span id="L1193">KHTH_MIN = 0.0                  !   [m2 s-1] default = 0.0</span>
<span id="L1194">                                ! The minimum horizontal thickness diffusivity.</span>
<span id="L1195">KHTH_MAX = 900.0                !   [m2 s-1] default = 0.0</span>
<span id="L1196">                                ! The maximum horizontal thickness diffusivity.</span>
<span id="L1197">KHTH_MAX_CFL = 0.8              !   [nondimensional] default = 0.8</span>
<span id="L1198">                                ! The maximum value of the local diffusive CFL ratio that is permitted for the</span>
<span id="L1199">                                ! thickness diffusivity. 1.0 is the marginally unstable value in a pure layered</span>
<span id="L1200">                                ! model, but much smaller numbers (e.g. 0.1) seem to work better for ALE-based</span>
<span id="L1201">                                ! models.</span>
<span id="L1202">KH_ETA_CONST = 0.0              !   [m2 s-1] default = 0.0</span>
<span id="L1203">                                ! The background horizontal diffusivity of the interface heights (without</span>
<span id="L1204">                                ! considering the layer density structure).  If diffusive CFL limits are</span>
<span id="L1205">                                ! encountered, the diffusivities of the isopycnals and the interfaces heights</span>
<span id="L1206">                                ! are scaled back proportionately.</span>
<span id="L1207">KH_ETA_VEL_SCALE = 0.0          !   [m s-1] default = 0.0</span>
<span id="L1208">                                ! A velocity scale that is multiplied by the grid spacing to give a contribution</span>
<span id="L1209">                                ! to the horizontal diffusivity of the interface heights (without considering</span>
<span id="L1210">                                ! the layer density structure).</span>
<span id="L1211">DETANGLE_INTERFACES = False     !   [Boolean] default = False</span>
<span id="L1212">                                ! If defined add 3-d structured enhanced interface height diffusivities to</span>
<span id="L1213">                                ! horizontally smooth jagged layers.</span>
<span id="L1214">KHTH_SLOPE_MAX = 0.01           !   [nondim] default = 0.01</span>
<span id="L1215">                                ! A slope beyond which the calculated isopycnal slope is not reliable and is</span>
<span id="L1216">                                ! scaled away.</span>
<span id="L1217">KHTH_USE_FGNV_STREAMFUNCTION = True !   [Boolean] default = False</span>
<span id="L1218">                                ! If true, use the streamfunction formulation of Ferrari et al., 2010, which</span>
<span id="L1219">                                ! effectively emphasizes graver vertical modes by smoothing in the vertical.</span>
<span id="L1220">FGNV_FILTER_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1221">                                ! A coefficient scaling the vertical smoothing term in the Ferrari et al., 2010,</span>
<span id="L1222">                                ! streamfunction formulation.</span>
<span id="L1223">FGNV_C_MIN = 0.01               !   [m s-1] default = 0.0</span>
<span id="L1224">                                ! A minium wave speed used in the Ferrari et al., 2010, streamfunction</span>
<span id="L1225">                                ! formulation.</span>
<span id="L1226">FGNV_STRAT_FLOOR = 1.0E-15      !   [nondim] default = 1.0E-15</span>
<span id="L1227">                                ! A floor for Brunt-Vasaila frequency in the Ferrari et al., 2010,</span>
<span id="L1228">                                ! streamfunction formulation, expressed as a fraction of planetary rotation,</span>
<span id="L1229">                                ! OMEGA. This should be tiny but non-zero to avoid degeneracy.</span>
<span id="L1230">USE_STANLEY_GM = False          !   [Boolean] default = False</span>
<span id="L1231">                                ! If true, turn on Stanley SGS T variance parameterization in GM code.</span>
<span id="L1232">USE_KH_IN_MEKE = False          !   [Boolean] default = False</span>
<span id="L1233">                                ! If true, uses the thickness diffusivity calculated here to diffuse MEKE.</span>
<span id="L1234">USE_GME = False                 !   [Boolean] default = False</span>
<span id="L1235">                                ! If true, use the GM+E backscatter scheme in association with the Gent and</span>
<span id="L1236">                                ! McWilliams parameterization.</span>
<span id="L1237">USE_GM_WORK_BUG = False         !   [Boolean] default = False</span>
<span id="L1238">                                ! If true, compute the top-layer work tendency on the u-grid with the incorrect</span>
<span id="L1239">                                ! sign, for legacy reproducibility.</span>
<span id="L1240">STOCH_EOS = False               !   [Boolean] default = False</span>
<span id="L1241">                                ! If true, stochastic perturbations are applied to the EOS in the PGF.</span>
<span id="L1242">STANLEY_COEFF = -1.0            !   [nondim] default = -1.0</span>
<span id="L1243">                                ! Coefficient correlating the temperature gradient and SGS T variance.</span>
<span id="L1244"></span>
<span id="L1245">! === module MOM_dynamics_split_RK2 ===</span>
<span id="L1246">TIDES = True                    !   [Boolean] default = False</span>
<span id="L1247">                                ! If true, apply tidal momentum forcing.</span>
<span id="L1248">CALCULATE_SAL = True            !   [Boolean] default = True</span>
<span id="L1249">                                ! If true, calculate self-attraction and loading.</span>
<span id="L1250">USE_HA = False                  !   [Boolean] default = False</span>
<span id="L1251">                                ! If true, perform inline harmonic analysis.</span>
<span id="L1252">BE = 0.6                        !   [nondim] default = 0.6</span>
<span id="L1253">                                ! If SPLIT is true, BE determines the relative weighting of a  2nd-order</span>
<span id="L1254">                                ! Runga-Kutta baroclinic time stepping scheme (0.5) and a backward Euler scheme</span>
<span id="L1255">                                ! (1) that is used for the Coriolis and inertial terms.  BE may be from 0.5 to</span>
<span id="L1256">                                ! 1, but instability may occur near 0.5. BE is also applicable if SPLIT is false</span>
<span id="L1257">                                ! and USE_RK2 is true.</span>
<span id="L1258">BEGW = 0.0                      !   [nondim] default = 0.0</span>
<span id="L1259">                                ! If SPLIT is true, BEGW is a number from 0 to 1 that controls the extent to</span>
<span id="L1260">                                ! which the treatment of gravity waves is forward-backward (0) or simulated</span>
<span id="L1261">                                ! backward Euler (1).  0 is almost always used. If SPLIT is false and USE_RK2 is</span>
<span id="L1262">                                ! true, BEGW can be between 0 and 0.5 to damp gravity waves.</span>
<span id="L1263">SET_DTBT_USE_BT_CONT = False    !   [Boolean] default = False</span>
<span id="L1264">                                ! If true, use BT_CONT to calculate DTBT if possible.</span>
<span id="L1265">SPLIT_BOTTOM_STRESS = False     !   [Boolean] default = False</span>
<span id="L1266">                                ! If true, provide the bottom stress calculated by the vertical viscosity to the</span>
<span id="L1267">                                ! barotropic solver.</span>
<span id="L1268">BT_USE_LAYER_FLUXES = True      !   [Boolean] default = True</span>
<span id="L1269">                                ! If true, use the summed layered fluxes plus an adjustment due to the change in</span>
<span id="L1270">                                ! the barotropic velocity in the barotropic continuity equation.</span>
<span id="L1271">BT_ADJ_CORR_MASS_SRC = True     !   [Boolean] default = True</span>
<span id="L1272">                                ! If true, recalculates the barotropic mass source after predictor step. This</span>
<span id="L1273">                                ! should make little difference in the deep ocean but appears to help for</span>
<span id="L1274">                                ! vanished layers. If false, uses the same mass source as from the predictor</span>
<span id="L1275">                                ! step.</span>
<span id="L1276">STORE_CORIOLIS_ACCEL = True     !   [Boolean] default = True</span>
<span id="L1277">                                ! If true, calculate the Coriolis accelerations at the end of each timestep for</span>
<span id="L1278">                                ! use in the predictor step of the next split RK2 timestep.</span>
<span id="L1279">FPMIX = False                   !   [Boolean] default = False</span>
<span id="L1280">                                ! If true, add non-local momentum flux increments and diffuse down the Eulerian</span>
<span id="L1281">                                ! gradient.</span>
<span id="L1282">VISC_REM_BUG = True             !   [Boolean] default = False</span>
<span id="L1283">                                ! If true, visc_rem_[uv] in split mode is incorrectly calculated or accounted</span>
<span id="L1284">                                ! for in two places. This parameter controls the defaults of two individual</span>
<span id="L1285">                                ! flags, VISC_REM_TIMESTEP_BUG in MOM_dynamics_split_RK2(b) and</span>
<span id="L1286">                                ! VISC_REM_BT_WEIGHT_BUG in MOM_barotropic.</span>
<span id="L1287">VISC_REM_TIMESTEP_BUG = True    !   [Boolean] default = True</span>
<span id="L1288">                                ! If true, recover a bug that uses dt_pred rather than dt in vertvisc_remnant()</span>
<span id="L1289">                                ! at the end of predictor stage for the following continuity() and btstep()</span>
<span id="L1290">                                ! calls in the corrector step. Default of this flag is set by VISC_REM_BUG</span>
<span id="L1291"></span>
<span id="L1292">! === module MOM_continuity_PPM ===</span>
<span id="L1293">MONOTONIC_CONTINUITY = False    !   [Boolean] default = False</span>
<span id="L1294">                                ! If true, CONTINUITY_PPM uses the Colella and Woodward monotonic limiter.  The</span>
<span id="L1295">                                ! default (false) is to use a simple positive definite limiter.</span>
<span id="L1296">SIMPLE_2ND_PPM_CONTINUITY = False !   [Boolean] default = False</span>
<span id="L1297">                                ! If true, CONTINUITY_PPM uses a simple 2nd order (arithmetic mean)</span>
<span id="L1298">                                ! interpolation of the edge values. This may give better PV conservation</span>
<span id="L1299">                                ! properties. While it formally reduces the accuracy of the continuity solver</span>
<span id="L1300">                                ! itself in the strongly advective limit, it does not reduce the overall order</span>
<span id="L1301">                                ! of accuracy of the dynamic core.</span>
<span id="L1302">UPWIND_1ST_CONTINUITY = False   !   [Boolean] default = False</span>
<span id="L1303">                                ! If true, CONTINUITY_PPM becomes a 1st-order upwind continuity solver.  This</span>
<span id="L1304">                                ! scheme is highly diffusive but may be useful for debugging or in single-column</span>
<span id="L1305">                                ! mode where its minimal stencil is useful.</span>
<span id="L1306">ETA_TOLERANCE = 1.0E-06         !   [m] default = 2.5E-09</span>
<span id="L1307">                                ! The tolerance for the differences between the barotropic and baroclinic</span>
<span id="L1308">                                ! estimates of the sea surface height due to the fluxes through each face.  The</span>
<span id="L1309">                                ! total tolerance for SSH is 4 times this value.  The default is</span>
<span id="L1310">                                ! 0.5*NK*ANGSTROM, and this should not be set less than about</span>
<span id="L1311">                                ! 10^-15*MAXIMUM_DEPTH.</span>
<span id="L1312">VELOCITY_TOLERANCE = 1.0E-04    !   [m s-1] default = 3.0E+08</span>
<span id="L1313">                                ! The tolerance for barotropic velocity discrepancies between the barotropic</span>
<span id="L1314">                                ! solution and  the sum of the layer thicknesses.</span>
<span id="L1315">CONT_PPM_AGGRESS_ADJUST = False !   [Boolean] default = False</span>
<span id="L1316">                                ! If true, allow the adjusted velocities to have a relative CFL change up to</span>
<span id="L1317">                                ! 0.5.</span>
<span id="L1318">CONT_PPM_VOLUME_BASED_CFL = False !   [Boolean] default = False</span>
<span id="L1319">                                ! If true, use the ratio of the open face lengths to the tracer cell areas when</span>
<span id="L1320">                                ! estimating CFL numbers.  The default is set by CONT_PPM_AGGRESS_ADJUST.</span>
<span id="L1321">CONTINUITY_CFL_LIMIT = 0.5      !   [nondim] default = 0.5</span>
<span id="L1322">                                ! The maximum CFL of the adjusted velocities.</span>
<span id="L1323">CONT_PPM_BETTER_ITER = True     !   [Boolean] default = True</span>
<span id="L1324">                                ! If true, stop corrective iterations using a velocity based criterion and only</span>
<span id="L1325">                                ! stop if the iteration is better than all predecessors.</span>
<span id="L1326">CONT_PPM_USE_VISC_REM_MAX = True !   [Boolean] default = True</span>
<span id="L1327">                                ! If true, use more appropriate limiting bounds for corrections in strongly</span>
<span id="L1328">                                ! viscous columns.</span>
<span id="L1329">CONT_PPM_MARGINAL_FACE_AREAS = True !   [Boolean] default = True</span>
<span id="L1330">                                ! If true, use the marginal face areas from the continuity solver for use as the</span>
<span id="L1331">                                ! weights in the barotropic solver. Otherwise use the transport averaged areas.</span>
<span id="L1332"></span>
<span id="L1333">! === module MOM_CoriolisAdv ===</span>
<span id="L1334">NOSLIP = False                  !   [Boolean] default = False</span>
<span id="L1335">                                ! If true, no slip boundary conditions are used; otherwise free slip boundary</span>
<span id="L1336">                                ! conditions are assumed. The implementation of the free slip BCs on a C-grid is</span>
<span id="L1337">                                ! much cleaner than the no slip BCs. The use of free slip BCs is strongly</span>
<span id="L1338">                                ! encouraged, and no slip BCs are not used with the biharmonic viscosity.</span>
<span id="L1339">CORIOLIS_EN_DIS = False         !   [Boolean] default = False</span>
<span id="L1340">                                ! If true, two estimates of the thickness fluxes are used to estimate the</span>
<span id="L1341">                                ! Coriolis term, and the one that dissipates energy relative to the other one is</span>
<span id="L1342">                                ! used.</span>
<span id="L1343">CORIOLIS_SCHEME = &quot;SADOURNY75_ENERGY&quot; ! default = &quot;SADOURNY75_ENERGY&quot;</span>
<span id="L1344">                                ! CORIOLIS_SCHEME selects the discretization for the Coriolis terms. Valid</span>
<span id="L1345">                                ! values are:</span>
<span id="L1346">                                !    SADOURNY75_ENERGY - Sadourny, 1975; energy cons.</span>
<span id="L1347">                                !    ARAKAWA_HSU90     - Arakawa &amp; Hsu, 1990</span>
<span id="L1348">                                !    SADOURNY75_ENSTRO - Sadourny, 1975; enstrophy cons.</span>
<span id="L1349">                                !    ARAKAWA_LAMB81    - Arakawa &amp; Lamb, 1981; En. + Enst.</span>
<span id="L1350">                                !    ARAKAWA_LAMB_BLEND - A blend of Arakawa &amp; Lamb with</span>
<span id="L1351">                                !                         Arakawa &amp; Hsu and Sadourny energy</span>
<span id="L1352">                                !    WENOVI5TH_PV_ENSTRO   - 5th-order WENO PV enstrophy</span>
<span id="L1353">                                !    WENOVI3RD_PV_ENSTRO   - 3rd-order WENO PV enstrophy</span>
<span id="L1354">                                !    WENOVI7TH_PV_ENSTRO  - 7th-order WENO PV enstrophy</span>
<span id="L1355">BOUND_CORIOLIS = True           !   [Boolean] default = False</span>
<span id="L1356">                                ! If true, the Coriolis terms at u-points are bounded by the four estimates of</span>
<span id="L1357">                                ! (f+rv)v from the four neighboring v-points, and similarly at v-points.  This</span>
<span id="L1358">                                ! option would have no effect on the SADOURNY Coriolis scheme if it were</span>
<span id="L1359">                                ! possible to use centered difference thickness fluxes.</span>
<span id="L1360">KE_SCHEME = &quot;KE_ARAKAWA&quot;        ! default = &quot;KE_ARAKAWA&quot;</span>
<span id="L1361">                                ! KE_SCHEME selects the discretization for acceleration due to the kinetic</span>
<span id="L1362">                                ! energy gradient. Valid values are:</span>
<span id="L1363">                                !    KE_ARAKAWA, KE_SIMPLE_GUDONOV, KE_GUDONOV, KE_UP3</span>
<span id="L1364">PV_ADV_SCHEME = &quot;PV_ADV_CENTERED&quot; ! default = &quot;PV_ADV_CENTERED&quot;</span>
<span id="L1365">                                ! PV_ADV_SCHEME selects the discretization for PV advection. Valid values are:</span>
<span id="L1366">                                !    PV_ADV_CENTERED - centered (aka Sadourny, 75)</span>
<span id="L1367">                                !    PV_ADV_UPWIND1  - upwind, first order</span>
<span id="L1368"></span>
<span id="L1369">! === module MOM_self_attr_load ===</span>
<span id="L1370">SAL_USE_BPA = False             !   [Boolean] default = False</span>
<span id="L1371">                                ! If true, use bottom pressure anomaly to calculate self-attraction and loading</span>
<span id="L1372">                                ! (SAL). Otherwise sea surface height anomaly is used, which is only accurate</span>
<span id="L1373">                                ! for uniform density fluid.</span>
<span id="L1374">SAL_SCALAR_APPROX = True        !   [Boolean] default = True</span>
<span id="L1375">                                ! If true, use the scalar approximation to calculate self-attraction and</span>
<span id="L1376">                                ! loading.</span>
<span id="L1377">SAL_SCALAR_VALUE = 0.094        !   [m m-1] default = 0.0</span>
<span id="L1378">                                ! The constant of proportionality between self-attraction and loading (SAL)</span>
<span id="L1379">                                ! geopotential anomaly and barotropic geopotential anomaly. This is only used if</span>
<span id="L1380">                                ! SAL_SCALAR_APPROX is true or USE_PREVIOUS_TIDES is true.</span>
<span id="L1381">SAL_HARMONICS = False           !   [Boolean] default = False</span>
<span id="L1382">                                ! If true, use the online spherical harmonics method to calculate</span>
<span id="L1383">                                ! self-attraction and loading.</span>
<span id="L1384"></span>
<span id="L1385">! === module MOM_tidal_forcing ===</span>
<span id="L1386">TIDE_M2 = True                  !   [Boolean] default = False</span>
<span id="L1387">                                ! If true, apply tidal momentum forcing at the M2 frequency. This is only used</span>
<span id="L1388">                                ! if TIDES is true.</span>
<span id="L1389">TIDE_S2 = False                 !   [Boolean] default = False</span>
<span id="L1390">                                ! If true, apply tidal momentum forcing at the S2 frequency. This is only used</span>
<span id="L1391">                                ! if TIDES is true.</span>
<span id="L1392">TIDE_N2 = False                 !   [Boolean] default = False</span>
<span id="L1393">                                ! If true, apply tidal momentum forcing at the N2 frequency. This is only used</span>
<span id="L1394">                                ! if TIDES is true.</span>
<span id="L1395">TIDE_K2 = False                 !   [Boolean] default = False</span>
<span id="L1396">                                ! If true, apply tidal momentum forcing at the K2 frequency. This is only used</span>
<span id="L1397">                                ! if TIDES is true.</span>
<span id="L1398">TIDE_K1 = False                 !   [Boolean] default = False</span>
<span id="L1399">                                ! If true, apply tidal momentum forcing at the K1 frequency. This is only used</span>
<span id="L1400">                                ! if TIDES is true.</span>
<span id="L1401">TIDE_O1 = False                 !   [Boolean] default = False</span>
<span id="L1402">                                ! If true, apply tidal momentum forcing at the O1 frequency. This is only used</span>
<span id="L1403">                                ! if TIDES is true.</span>
<span id="L1404">TIDE_P1 = False                 !   [Boolean] default = False</span>
<span id="L1405">                                ! If true, apply tidal momentum forcing at the P1 frequency. This is only used</span>
<span id="L1406">                                ! if TIDES is true.</span>
<span id="L1407">TIDE_Q1 = False                 !   [Boolean] default = False</span>
<span id="L1408">                                ! If true, apply tidal momentum forcing at the Q1 frequency. This is only used</span>
<span id="L1409">                                ! if TIDES is true.</span>
<span id="L1410">TIDE_MF = False                 !   [Boolean] default = False</span>
<span id="L1411">                                ! If true, apply tidal momentum forcing at the MF frequency. This is only used</span>
<span id="L1412">                                ! if TIDES is true.</span>
<span id="L1413">TIDE_MM = False                 !   [Boolean] default = False</span>
<span id="L1414">                                ! If true, apply tidal momentum forcing at the MM frequency. This is only used</span>
<span id="L1415">                                ! if TIDES is true.</span>
<span id="L1416">TIDAL_SAL_FROM_FILE = False     !   [Boolean] default = False</span>
<span id="L1417">                                ! If true, read the tidal self-attraction and loading from input files,</span>
<span id="L1418">                                ! specified by TIDAL_INPUT_FILE. This is only used if TIDES is true.</span>
<span id="L1419">USE_PREVIOUS_TIDES = False      !   [Boolean] default = False</span>
<span id="L1420">                                ! If true, use the SAL from the previous iteration of the tides to facilitate</span>
<span id="L1421">                                ! convergent iteration. This is only used if TIDES is true.</span>
<span id="L1422">TIDE_REF_DATE = 0, 0, 0         ! default = 0, 0, 0</span>
<span id="L1423">                                ! Year,month,day to use as reference date for tidal forcing. If not specified,</span>
<span id="L1424">                                ! defaults to 0.</span>
<span id="L1425">TIDE_USE_EQ_PHASE = False       !   [Boolean] default = False</span>
<span id="L1426">                                ! Correct phases by calculating equilibrium phase arguments for TIDE_REF_DATE.</span>
<span id="L1427">TIDE_M2_FREQ = 1.405189E-04     !   [rad s-1] default = 1.405189E-04</span>
<span id="L1428">                                ! Frequency of the M2 tidal constituent. This is only used if TIDES and TIDE_M2</span>
<span id="L1429">                                ! are true, or if OBC_TIDE_N_CONSTITUENTS &gt; 0 and M2 is in</span>
<span id="L1430">                                ! OBC_TIDE_CONSTITUENTS.</span>
<span id="L1431">TIDE_M2_AMP = 0.242334          !   [m] default = 0.242334</span>
<span id="L1432">                                ! Amplitude of the M2 tidal constituent. This is only used if TIDES and TIDE_M2</span>
<span id="L1433">                                ! are true.</span>
<span id="L1434">TIDE_M2_PHASE_T0 = 0.0          !   [radians] default = 0.0</span>
<span id="L1435">                                ! Phase of the M2 tidal constituent at time 0. This is only used if TIDES and</span>
<span id="L1436">                                ! TIDE_M2 are true.</span>
<span id="L1437">TIDE_ADD_NODAL = False          !   [Boolean] default = False</span>
<span id="L1438">                                ! If true, include 18.6 year nodal modulation in the astronomical tidal forcing.</span>
<span id="L1439">TIDE_NODAL_REF_DATE = 0, 0, 0   ! default = 0, 0, 0</span>
<span id="L1440">                                ! Fixed reference date to use for nodal modulation of astronomical tidal</span>
<span id="L1441">                                ! forcing.</span>
<span id="L1442"></span>
<span id="L1443">! === module MOM_PressureForce ===</span>
<span id="L1444">ANALYTIC_FV_PGF = True          !   [Boolean] default = True</span>
<span id="L1445">                                ! If true the pressure gradient forces are calculated with a finite volume form</span>
<span id="L1446">                                ! that analytically integrates the equations of state in pressure to avoid any</span>
<span id="L1447">                                ! possibility of numerical thermobaric instability, as described in Adcroft et</span>
<span id="L1448">                                ! al., O. Mod. (2008).</span>
<span id="L1449"></span>
<span id="L1450">! === module MOM_PressureForce_FV ===</span>
<span id="L1451">RHO_PGF_REF = 1035.0            !   [kg m-3] default = 1035.0</span>
<span id="L1452">                                ! The reference density that is subtracted off when calculating pressure</span>
<span id="L1453">                                ! gradient forces.  Its inverse is subtracted off of specific volumes when in</span>
<span id="L1454">                                ! non-Boussinesq mode.  The default is RHO_0.</span>
<span id="L1455">RHO_PGF_REF_BUG = True          !   [Boolean] default = True</span>
<span id="L1456">                                ! If true, recover a bug that RHO_0 (the mean seawater density in Boussinesq</span>
<span id="L1457">                                ! mode) and RHO_PGF_REF (the subtracted reference density in finite volume</span>
<span id="L1458">                                ! pressure gradient forces) are incorrectly interchanged in several instances in</span>
<span id="L1459">                                ! Boussinesq mode.</span>
<span id="L1460">TIDES_ANSWER_DATE = 20230630    ! default = 99991231</span>
<span id="L1461">                                ! The vintage of self-attraction and loading (SAL) and tidal forcing</span>
<span id="L1462">                                ! calculations.  Setting dates before 20230701 recovers old answers (Boussinesq</span>
<span id="L1463">                                ! and non-Boussinesq modes) when SAL is part of the tidal forcing calculation.</span>
<span id="L1464">                                ! The answer difference is only at bit level and due to a reordered summation.</span>
<span id="L1465">                                ! Setting dates before 20250201 recovers answers (Boussinesq mode) that</span>
<span id="L1466">                                ! interface heights are modified before pressure force integrals are calculated.</span>
<span id="L1467">BOUSSINESQ_SAL_TIDES = False    !   [Boolean] default = False</span>
<span id="L1468">                                ! If true, in Boussinesq mode, use an alternative method to include</span>
<span id="L1469">                                ! self-attraction and loading (SAL) and tidal forcings in pressure gradient, in</span>
<span id="L1470">                                ! which their gradients are calculated separately, instead of adding</span>
<span id="L1471">                                ! geopotential anomalies as corrections to the interface height.  This</span>
<span id="L1472">                                ! alternative method elimates a baroclinic component of the SAL and tidal</span>
<span id="L1473">                                ! forcings.</span>
<span id="L1474">SSH_IN_EOS_PRESSURE_FOR_PGF = False !   [Boolean] default = False</span>
<span id="L1475">                                ! If true, include contributions from the sea surface height in the height-based</span>
<span id="L1476">                                ! pressure used in the equation of state calculations for the Boussinesq</span>
<span id="L1477">                                ! pressure gradient forces, including adjustments for atmospheric or sea-ice</span>
<span id="L1478">                                ! pressure.</span>
<span id="L1479">MASS_WEIGHT_IN_PRESSURE_GRADIENT = True !   [Boolean] default = False</span>
<span id="L1480">                                ! If true, use mass weighting when interpolating T/S for integrals near the</span>
<span id="L1481">                                ! bathymetry in FV pressure gradient calculations.</span>
<span id="L1482">MASS_WEIGHT_IN_PRESSURE_GRADIENT_TOP = True !   [Boolean] default = True</span>
<span id="L1483">                                ! If true and MASS_WEIGHT_IN_PRESSURE_GRADIENT is true, use mass weighting when</span>
<span id="L1484">                                ! interpolating T/S for integrals near the top of the water column in FV</span>
<span id="L1485">                                ! pressure gradient calculations.</span>
<span id="L1486">MASS_WEIGHT_IN_PGF_VANISHED_ONLY = False !   [Boolean] default = False</span>
<span id="L1487">                                ! If true, use mass weighting when interpolating T/S for integrals only if one</span>
<span id="L1488">                                ! side is vanished according to RESET_INTXPA_H_NONVANISHED.</span>
<span id="L1489">CORRECTION_INTXPA = False       !   [Boolean] default = False</span>
<span id="L1490">                                ! If true, use a correction for surface pressure curvature in intx_pa.</span>
<span id="L1491">RESET_INTXPA_INTEGRAL = False   !   [Boolean] default = False</span>
<span id="L1492">                                ! If true, reset INTXPA to match pressures at first nonvanished cell. Includes</span>
<span id="L1493">                                ! pressure correction.</span>
<span id="L1494">RESET_INTXPA_INTEGRAL_FLATTEST = False !   [Boolean] default = False</span>
<span id="L1495">                                ! If true, use flattest interface as reference interface where there is no</span>
<span id="L1496">                                ! better choice for RESET_INTXPA_INTEGRAL. Otherwise, use surface interface.</span>
<span id="L1497">USE_INACCURATE_PGF_RHO_ANOM = False !   [Boolean] default = False</span>
<span id="L1498">                                ! If true, use a form of the PGF that uses the reference density in an</span>
<span id="L1499">                                ! inaccurate way. This is not recommended.</span>
<span id="L1500">RECONSTRUCT_FOR_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1501">                                ! If True, use vertical reconstruction of T &amp; S within the integrals of the FV</span>
<span id="L1502">                                ! pressure gradient calculation. If False, use the constant-by-layer algorithm.</span>
<span id="L1503">                                ! The default is set by USE_REGRIDDING.</span>
<span id="L1504">PRESSURE_RECONSTRUCTION_SCHEME = 1 ! default = 1</span>
<span id="L1505">                                ! Order of vertical reconstruction of T/S to use in the integrals within the FV</span>
<span id="L1506">                                ! pressure gradient calculation.</span>
<span id="L1507">                                !  0: PCM or no reconstruction.</span>
<span id="L1508">                                !  1: PLM reconstruction.</span>
<span id="L1509">                                !  2: PPM reconstruction.</span>
<span id="L1510">BOUNDARY_EXTRAPOLATION_PRESSURE = True !   [Boolean] default = True</span>
<span id="L1511">                                ! If true, the reconstruction of T &amp; S for pressure in boundary cells is</span>
<span id="L1512">                                ! extrapolated, rather than using PCM in these cells. If true, the same order</span>
<span id="L1513">                                ! polynomial is used as is used for the interior cells.</span>
<span id="L1514">USE_STANLEY_PGF = False         !   [Boolean] default = False</span>
<span id="L1515">                                ! If true, turn on Stanley SGS T variance parameterization in PGF code.</span>
<span id="L1516"></span>
<span id="L1517">! === module MOM_Zanna_Bolton ===</span>
<span id="L1518">USE_ZB2020 = False              !   [Boolean] default = False</span>
<span id="L1519">                                ! If true, turns on Zanna-Bolton-2020 (ZB) subgrid momentum parameterization of</span>
<span id="L1520">                                ! mesoscale eddies.</span>
<span id="L1521"></span>
<span id="L1522">! === module MOM_hor_visc ===</span>
<span id="L1523">USE_CIRCULATION_IN_HORVISC = False !   [Boolean] default = False</span>
<span id="L1524">                                ! Use circulation theorem to compute vorticity in horvisc module (for ZB20 or</span>
<span id="L1525">                                ! Leith)</span>
<span id="L1526">USE_CONT_THICKNESS = False      !   [Boolean] default = False</span>
<span id="L1527">                                ! If true, use thickness at velocity points from continuity solver. This option</span>
<span id="L1528">                                ! currently only works with split mode.</span>
<span id="L1529">LAPLACIAN = True                !   [Boolean] default = False</span>
<span id="L1530">                                ! If true, use a Laplacian horizontal viscosity.</span>
<span id="L1531">KH = 0.0                        !   [m2 s-1] default = 0.0</span>
<span id="L1532">                                ! The background Laplacian horizontal viscosity.</span>
<span id="L1533">KH_BG_MIN = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1534">                                ! The minimum value allowed for Laplacian horizontal viscosity, KH.</span>
<span id="L1535">KH_VEL_SCALE = 0.01             !   [m s-1] default = 0.0</span>
<span id="L1536">                                ! The velocity scale which is multiplied by the grid spacing to calculate the</span>
<span id="L1537">                                ! Laplacian viscosity. The final viscosity is the largest of this scaled</span>
<span id="L1538">                                ! viscosity, the Smagorinsky and Leith viscosities, and KH.</span>
<span id="L1539">KH_SIN_LAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1540">                                ! The amplitude of a latitudinally-dependent background viscosity of the form</span>
<span id="L1541">                                ! KH_SIN_LAT*(SIN(LAT)**KH_PWR_OF_SINE).</span>
<span id="L1542">SMAGORINSKY_KH = False          !   [Boolean] default = False</span>
<span id="L1543">                                ! If true, use a Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1544">LEITH_KH = False                !   [Boolean] default = False</span>
<span id="L1545">                                ! If true, use a Leith nonlinear eddy viscosity.</span>
<span id="L1546">RES_SCALE_MEKE_VISC = False     !   [Boolean] default = False</span>
<span id="L1547">                                ! If true, the viscosity contribution from MEKE is scaled by the resolution</span>
<span id="L1548">                                ! function.</span>
<span id="L1549">BOUND_KH = True                 !   [Boolean] default = True</span>
<span id="L1550">                                ! If true, the Laplacian coefficient is locally limited to be stable.</span>
<span id="L1551">EY24_EBT_BS = False             !   [Boolean] default = False</span>
<span id="L1552">                                ! If true, use the the backscatter scheme (EBT mode with kill switch)developed</span>
<span id="L1553">                                ! by Yankovsky et al. (2024).</span>
<span id="L1554">ANISOTROPIC_VISCOSITY = False   !   [Boolean] default = False</span>
<span id="L1555">                                ! If true, allow anistropic viscosity in the Laplacian horizontal viscosity.</span>
<span id="L1556">ADD_LES_VISCOSITY = False       !   [Boolean] default = False</span>
<span id="L1557">                                ! If true, adds the viscosity from Smagorinsky and Leith to the background</span>
<span id="L1558">                                ! viscosity instead of taking the maximum.</span>
<span id="L1559">BIHARMONIC = True               !   [Boolean] default = True</span>
<span id="L1560">                                ! If true, use a biharmonic horizontal viscosity. BIHARMONIC may be used with</span>
<span id="L1561">                                ! LAPLACIAN.</span>
<span id="L1562">AH = 0.0                        !   [m4 s-1] default = 0.0</span>
<span id="L1563">                                ! The background biharmonic horizontal viscosity.</span>
<span id="L1564">AH_VEL_SCALE = 0.05             !   [m s-1] default = 0.0</span>
<span id="L1565">                                ! The velocity scale which is multiplied by the cube of the grid spacing to</span>
<span id="L1566">                                ! calculate the biharmonic viscosity. The final viscosity is the largest of this</span>
<span id="L1567">                                ! scaled viscosity, the Smagorinsky and Leith viscosities, and AH.</span>
<span id="L1568">AH_TIME_SCALE = 0.0             !   [s] default = 0.0</span>
<span id="L1569">                                ! A time scale whose inverse is multiplied by the fourth power of the grid</span>
<span id="L1570">                                ! spacing to calculate biharmonic viscosity. The final viscosity is the largest</span>
<span id="L1571">                                ! of all viscosity formulations in use. 0.0 means that it&#x27;s not used.</span>
<span id="L1572">SMAGORINSKY_AH = True           !   [Boolean] default = False</span>
<span id="L1573">                                ! If true, use a biharmonic Smagorinsky nonlinear eddy viscosity.</span>
<span id="L1574">LEITH_AH = False                !   [Boolean] default = False</span>
<span id="L1575">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity.</span>
<span id="L1576">USE_LEITHY = False              !   [Boolean] default = False</span>
<span id="L1577">                                ! If true, use a biharmonic Leith nonlinear eddy viscosity together with a</span>
<span id="L1578">                                ! harmonic backscatter.</span>
<span id="L1579">BOUND_AH = True                 !   [Boolean] default = True</span>
<span id="L1580">                                ! If true, the biharmonic coefficient is locally limited to be stable.</span>
<span id="L1581">RE_AH = 0.0                     !   [nondim] default = 0.0</span>
<span id="L1582">                                ! If nonzero, the biharmonic coefficient is scaled so that the biharmonic</span>
<span id="L1583">                                ! Reynolds number is equal to this.</span>
<span id="L1584">BACKSCATTER_UNDERBOUND = True   !   [Boolean] default = False</span>
<span id="L1585">                                ! If true, the bounds on the biharmonic viscosity are allowed to increase where</span>
<span id="L1586">                                ! the Laplacian viscosity is negative (due to backscatter parameterizations)</span>
<span id="L1587">                                ! beyond the largest timestep-dependent stable values of biharmonic viscosity</span>
<span id="L1588">                                ! when no Laplacian viscosity is applied.  The default is true for historical</span>
<span id="L1589">                                ! reasons, but this option probably should not be used because it can contribute</span>
<span id="L1590">                                ! to numerical instabilities.</span>
<span id="L1591">SMAG_BI_CONST = 0.06            !   [nondim] default = 0.0</span>
<span id="L1592">                                ! The nondimensional biharmonic Smagorinsky constant, typically 0.015 - 0.06.</span>
<span id="L1593">BOUND_CORIOLIS_BIHARM = True    !   [Boolean] default = True</span>
<span id="L1594">                                ! If true use a viscosity that increases with the square of the velocity shears,</span>
<span id="L1595">                                ! so that the resulting viscous drag is of comparable magnitude to the Coriolis</span>
<span id="L1596">                                ! terms when the velocity differences between adjacent grid points is</span>
<span id="L1597">                                ! 0.5*BOUND_CORIOLIS_VEL.  The default is the value of BOUND_CORIOLIS (or</span>
<span id="L1598">                                ! false).</span>
<span id="L1599">BOUND_CORIOLIS_VEL = 6.0        !   [m s-1] default = 6.0</span>
<span id="L1600">                                ! The velocity scale at which BOUND_CORIOLIS_BIHARM causes the biharmonic drag</span>
<span id="L1601">                                ! to have comparable magnitude to the Coriolis acceleration.  The default is set</span>
<span id="L1602">                                ! by MAXVEL.</span>
<span id="L1603">USE_LAND_MASK_FOR_HVISC = True  !   [Boolean] default = True</span>
<span id="L1604">                                ! If true, use the land mask for the computation of thicknesses at velocity</span>
<span id="L1605">                                ! locations. This eliminates the dependence on arbitrary values over land or</span>
<span id="L1606">                                ! outside of the domain.</span>
<span id="L1607">HORVISC_BOUND_COEF = 0.8        !   [nondim] default = 0.8</span>
<span id="L1608">                                ! The nondimensional coefficient of the ratio of the viscosity bounds to the</span>
<span id="L1609">                                ! theoretical maximum for stability without considering other terms.</span>
<span id="L1610">USE_KH_BG_2D = False            !   [Boolean] default = False</span>
<span id="L1611">                                ! If true, read a file containing 2-d background harmonic viscosities. The final</span>
<span id="L1612">                                ! viscosity is the maximum of the other terms and this background value.</span>
<span id="L1613">FRICTWORK_BUG = False           !   [Boolean] default = False</span>
<span id="L1614">                                ! If true, retain an answer-changing bug in calculating the FrictWork, which</span>
<span id="L1615">                                ! cancels the h in thickness flux and the h at velocity point. This isnot</span>
<span id="L1616">                                ! recommended.</span>
<span id="L1617"></span>
<span id="L1618">! === module MOM_vert_friction ===</span>
<span id="L1619">VERT_FRICTION_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1620">                                ! The vintage of the order of arithmetic and expressions in the viscous</span>
<span id="L1621">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1622">                                ! while higher values use expressions that do not use an arbitrary hard-coded</span>
<span id="L1623">                                ! maximum viscous coupling coefficient between layers.  Values below 20230601</span>
<span id="L1624">                                ! recover a form of the viscosity within the mixed layer that breaks up the</span>
<span id="L1625">                                ! magnitude of the wind stress in some non-Boussinesq cases.</span>
<span id="L1626">DIRECT_STRESS = False           !   [Boolean] default = False</span>
<span id="L1627">                                ! If true, the wind stress is distributed over the topmost HMIX_STRESS of fluid</span>
<span id="L1628">                                ! (like in HYCOM), and an added mixed layer viscosity or a physically based</span>
<span id="L1629">                                ! boundary layer turbulence parameterization is not needed for stability.</span>
<span id="L1630">FIXED_DEPTH_LOTW_ML = False     !   [Boolean] default = False</span>
<span id="L1631">                                ! If true, use a Law-of-the-wall prescription for the mixed layer viscosity</span>
<span id="L1632">                                ! within a boundary layer that is the lesser of HMIX_FIXED and the total depth</span>
<span id="L1633">                                ! of the ocean in a column.</span>
<span id="L1634">LOTW_VISCOUS_ML_FLOOR = False   !   [Boolean] default = False</span>
<span id="L1635">                                ! If true, use a Law-of-the-wall prescription to set a lower bound on the</span>
<span id="L1636">                                ! viscous coupling between layers within the surface boundary layer, based the</span>
<span id="L1637">                                ! distance of interfaces from the surface.  This only acts when there are large</span>
<span id="L1638">                                ! changes in the thicknesses of successive layers or when the viscosity is set</span>
<span id="L1639">                                ! externally and the wind stress has subsequently increased.</span>
<span id="L1640">VON_KARMAN_CONST = 0.41         !   [nondim] default = 0.41</span>
<span id="L1641">                                ! The value the von Karman constant as used for mixed layer viscosity.</span>
<span id="L1642">HARMONIC_VISC = False           !   [Boolean] default = False</span>
<span id="L1643">                                ! If true, use the harmonic mean thicknesses for calculating the vertical</span>
<span id="L1644">                                ! viscosity.</span>
<span id="L1645">HARMONIC_BL_SCALE = 0.0         !   [nondim] default = 0.0</span>
<span id="L1646">                                ! A scale to determine when water is in the boundary layers based solely on</span>
<span id="L1647">                                ! harmonic mean thicknesses for the purpose of determining the extent to which</span>
<span id="L1648">                                ! the thicknesses used in the viscosities are upwinded.</span>
<span id="L1649">HMIX_FIXED = 0.5                !   [m]</span>
<span id="L1650">                                ! The prescribed depth over which the near-surface viscosity and diffusivity are</span>
<span id="L1651">                                ! elevated when the bulk mixed layer is not used.</span>
<span id="L1652">USE_GL90_IN_SSW = False         !   [Boolean] default = False</span>
<span id="L1653">                                ! If true, use simpler method to calculate 1/N^2 in GL90 vertical viscosity</span>
<span id="L1654">                                ! coefficient. This method is valid in stacked shallow water mode.</span>
<span id="L1655">KV_ML_INVZ2 = 0.0               !   [m2 s-1] default = 0.0</span>
<span id="L1656">                                ! An extra kinematic viscosity in a mixed layer of thickness HMIX_FIXED, with</span>
<span id="L1657">                                ! the actual viscosity scaling as 1/(z*HMIX_FIXED)^2, where z is the distance</span>
<span id="L1658">                                ! from the surface, to allow for finite wind stresses to be transmitted through</span>
<span id="L1659">                                ! infinitesimally thin surface layers.  This is an older option for numerical</span>
<span id="L1660">                                ! convenience without a strong physical basis, and its use is now discouraged.</span>
<span id="L1661">CFL_TRUNCATE = 0.5              !   [nondim] default = 0.5</span>
<span id="L1662">                                ! The value of the CFL number that will cause velocity components to be</span>
<span id="L1663">                                ! truncated; instability can occur past 0.5.</span>
<span id="L1664">CFL_REPORT = 0.5                !   [nondim] default = 0.5</span>
<span id="L1665">                                ! The value of the CFL number that causes accelerations to be reported; the</span>
<span id="L1666">                                ! default is CFL_TRUNCATE.</span>
<span id="L1667">CFL_TRUNCATE_RAMP_TIME = 7200.0 !   [s] default = 0.0</span>
<span id="L1668">                                ! The time over which the CFL truncation value is ramped up at the beginning of</span>
<span id="L1669">                                ! the run.</span>
<span id="L1670">CFL_TRUNCATE_START = 0.0        !   [nondim] default = 0.0</span>
<span id="L1671">                                ! The start value of the truncation CFL number used when ramping up CFL_TRUNC.</span>
<span id="L1672">STOKES_MIXING_COMBINED = False  !   [Boolean] default = False</span>
<span id="L1673">                                ! Flag to use Stokes drift Mixing via the Lagrangian  current (Eulerian plus</span>
<span id="L1674">                                ! Stokes drift).  Still needs work and testing, so not recommended for use.</span>
<span id="L1675">VEL_UNDERFLOW = 0.0             !   [m s-1] default = 0.0</span>
<span id="L1676">                                ! A negligibly small velocity magnitude below which velocity components are set</span>
<span id="L1677">                                ! to 0.  A reasonable value might be 1e-30 m/s, which is less than an Angstrom</span>
<span id="L1678">                                ! divided by the age of the universe.</span>
<span id="L1679"></span>
<span id="L1680">! === module MOM_barotropic ===</span>
<span id="L1681">USE_BT_CONT_TYPE = True         !   [Boolean] default = True</span>
<span id="L1682">                                ! If true, use a structure with elements that describe effective face areas from</span>
<span id="L1683">                                ! the summed continuity solver as a function the barotropic flow in coupling</span>
<span id="L1684">                                ! between the barotropic and baroclinic flow.  This is only used if SPLIT is</span>
<span id="L1685">                                ! true.</span>
<span id="L1686">INTEGRAL_BT_CONTINUITY = False  !   [Boolean] default = False</span>
<span id="L1687">                                ! If true, use the time-integrated velocity over the barotropic steps to</span>
<span id="L1688">                                ! determine the integrated transports used to update the continuity equation.</span>
<span id="L1689">                                ! Otherwise the transports are the sum of the transports based on a series of</span>
<span id="L1690">                                ! instantaneous velocities and the BT_CONT_TYPE for transports.  This is only</span>
<span id="L1691">                                ! valid if USE_BT_CONT_TYPE = True.</span>
<span id="L1692">BOUND_BT_CORRECTION = True      !   [Boolean] default = False</span>
<span id="L1693">                                ! If true, the corrective pseudo mass-fluxes into the barotropic solver are</span>
<span id="L1694">                                ! limited to values that require less than maxCFL_BT_cont to be accommodated.</span>
<span id="L1695">BT_CONT_CORR_BOUNDS = True      !   [Boolean] default = True</span>
<span id="L1696">                                ! If true, and BOUND_BT_CORRECTION is true, use the BT_cont_type variables to</span>
<span id="L1697">                                ! set limits determined by MAXCFL_BT_CONT on the CFL number of the velocities</span>
<span id="L1698">                                ! that are likely to be driven by the corrective mass fluxes.</span>
<span id="L1699">ADJUST_BT_CONT = False          !   [Boolean] default = False</span>
<span id="L1700">                                ! If true, adjust the curve fit to the BT_cont type that is used by the</span>
<span id="L1701">                                ! barotropic solver to match the transport about which the flow is being</span>
<span id="L1702">                                ! linearized.</span>
<span id="L1703">GRADUAL_BT_ICS = False          !   [Boolean] default = False</span>
<span id="L1704">                                ! If true, adjust the initial conditions for the barotropic solver to the values</span>
<span id="L1705">                                ! from the layered solution over a whole timestep instead of instantly. This is</span>
<span id="L1706">                                ! a decent approximation to the inclusion of sum(u dh_dt) while also correcting</span>
<span id="L1707">                                ! for truncation errors.</span>
<span id="L1708">BT_USE_VISC_REM_U_UH0 = False   !   [Boolean] default = False</span>
<span id="L1709">                                ! If true, use the viscous remnants when estimating the barotropic velocities</span>
<span id="L1710">                                ! that were used to calculate uh0 and vh0.  False is probably the better choice.</span>
<span id="L1711">BT_PROJECT_VELOCITY = True      !   [Boolean] default = False</span>
<span id="L1712">                                ! If true, step the barotropic velocity first and project out the velocity</span>
<span id="L1713">                                ! tendency by 1+BEBT when calculating the transport.  The default (false) is to</span>
<span id="L1714">                                ! use a predictor continuity step to find the pressure field, and then to do a</span>
<span id="L1715">                                ! corrector continuity step using a weighted average of the old and new</span>
<span id="L1716">                                ! velocities, with weights of (1-BEBT) and BEBT.</span>
<span id="L1717">BT_NONLIN_STRESS = False        !   [Boolean] default = False</span>
<span id="L1718">                                ! If true, use the full depth of the ocean at the start of the barotropic step</span>
<span id="L1719">                                ! when calculating the surface stress contribution to the barotropic</span>
<span id="L1720">                                ! acclerations.  Otherwise use the depth based on bathyT.</span>
<span id="L1721">DYNAMIC_SURFACE_PRESSURE = False !   [Boolean] default = False</span>
<span id="L1722">                                ! If true, add a dynamic pressure due to a viscous ice shelf, for instance.</span>
<span id="L1723">BT_CORIOLIS_SCALE = 1.0         !   [nondim] default = 1.0</span>
<span id="L1724">                                ! A factor by which the barotropic Coriolis anomaly terms are scaled.</span>
<span id="L1725">BAROTROPIC_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1726">                                ! The vintage of the expressions in the barotropic solver. Values below 20190101</span>
<span id="L1727">                                ! recover the answers from the end of 2018, while higher values use more</span>
<span id="L1728">                                ! efficient or general expressions.</span>
<span id="L1729">VISC_REM_BT_WEIGHT_BUG = True   !   [Boolean] default = True</span>
<span id="L1730">                                ! If true, recover a bug in barotropic solver that uses an unnormalized weight</span>
<span id="L1731">                                ! function for vertical averages of baroclinic velocity and forcing. Default of</span>
<span id="L1732">                                ! this flag is set by VISC_REM_BUG.</span>
<span id="L1733">BAROTROPIC_TIDAL_SAL_BUG = False !   [Boolean] default = False</span>
<span id="L1734">                                ! If true, the tidal self-attraction and loading anomaly in the barotropic</span>
<span id="L1735">                                ! solver has the wrong sign, replicating a long-standing bug with a scalar</span>
<span id="L1736">                                ! self-attraction and loading term or the SAL term from a previous simulation.</span>
<span id="L1737">TIDAL_SAL_FLATHER = False       !   [Boolean] default = False</span>
<span id="L1738">                                ! If true, then apply adjustments to the external gravity wave speed used with</span>
<span id="L1739">                                ! the Flather OBC routine consistent with the barotropic solver. This applies to</span>
<span id="L1740">                                ! cases with  tidal forcing using the scalar self-attraction approximation. The</span>
<span id="L1741">                                ! default is currently False in order to retain previous answers but should be</span>
<span id="L1742">                                ! set to True for new experiments</span>
<span id="L1743">SADOURNY = True                 !   [Boolean] default = True</span>
<span id="L1744">                                ! If true, the Coriolis terms are discretized with the Sadourny (1975) energy</span>
<span id="L1745">                                ! conserving scheme, otherwise the Arakawa &amp; Hsu scheme is used.  If the</span>
<span id="L1746">                                ! internal deformation radius is not resolved, the Sadourny scheme should</span>
<span id="L1747">                                ! probably be used.</span>
<span id="L1748">BT_THICK_SCHEME = &quot;FROM_BT_CONT&quot; ! default = &quot;FROM_BT_CONT&quot;</span>
<span id="L1749">                                ! A string describing the scheme that is used to set the open face areas used</span>
<span id="L1750">                                ! for barotropic transport and the relative weights of the accelerations. Valid</span>
<span id="L1751">                                ! values are:</span>
<span id="L1752">                                !    ARITHMETIC - arithmetic mean layer thicknesses</span>
<span id="L1753">                                !    HARMONIC - harmonic mean layer thicknesses</span>
<span id="L1754">                                !    HYBRID (the default) - use arithmetic means for</span>
<span id="L1755">                                !       layers above the shallowest bottom, the harmonic</span>
<span id="L1756">                                !       mean for layers below, and a weighted average for</span>
<span id="L1757">                                !       layers that straddle that depth</span>
<span id="L1758">                                !    FROM_BT_CONT - use the average thicknesses kept</span>
<span id="L1759">                                !       in the h_u and h_v fields of the BT_cont_type</span>
<span id="L1760">BT_STRONG_DRAG = False          !   [Boolean] default = False</span>
<span id="L1761">                                ! If true, use a stronger estimate of the retarding effects of strong bottom</span>
<span id="L1762">                                ! drag, by making it implicit with the barotropic time-step instead of implicit</span>
<span id="L1763">                                ! with the baroclinic time-step and dividing by the number of barotropic steps.</span>
<span id="L1764">BT_LINEAR_WAVE_DRAG = False     !   [Boolean] default = False</span>
<span id="L1765">                                ! If true, apply a linear drag to the barotropic velocities, using rates set by</span>
<span id="L1766">                                ! lin_drag_u &amp; _v divided by the depth of the ocean.  This was introduced to</span>
<span id="L1767">                                ! facilitate tide modeling.</span>
<span id="L1768">BT_LINEAR_FREQ_DRAG = False     !   [Boolean] default = False</span>
<span id="L1769">                                ! If true, apply frequency-dependent drag to the tidal velocities. The streaming</span>
<span id="L1770">                                ! band-pass filter must be turned on.</span>
<span id="L1771">CLIP_BT_VELOCITY = False        !   [Boolean] default = False</span>
<span id="L1772">                                ! If true, limit any velocity components that exceed CFL_TRUNCATE.  This should</span>
<span id="L1773">                                ! only be used as a desperate debugging measure.</span>
<span id="L1774">MAXCFL_BT_CONT = 0.25           !   [nondim] default = 0.25</span>
<span id="L1775">                                ! The maximum permitted CFL number associated with the barotropic accelerations</span>
<span id="L1776">                                ! from the summed velocities times the time-derivatives of thicknesses.</span>
<span id="L1777">DT_BT_FILTER = -0.25            !   [sec or nondim] default = -0.25</span>
<span id="L1778">                                ! A time-scale over which the barotropic mode solutions are filtered, in seconds</span>
<span id="L1779">                                ! if positive, or as a fraction of DT if negative. When used this can never be</span>
<span id="L1780">                                ! taken to be longer than 2*dt.  Set this to 0 to apply no filtering.</span>
<span id="L1781">G_BT_EXTRA = 0.0                !   [nondim] default = 0.0</span>
<span id="L1782">                                ! A nondimensional factor by which gtot is enhanced.</span>
<span id="L1783">SSH_EXTRA = 10.0                !   [m] default = 10.0</span>
<span id="L1784">                                ! An estimate of how much higher SSH might get, for use in calculating the safe</span>
<span id="L1785">                                ! external wave speed. The default is the minimum of 10 m or 5% of</span>
<span id="L1786">                                ! MAXIMUM_DEPTH.</span>
<span id="L1787">LINEARIZED_BT_CORIOLIS = True   !   [Boolean] default = True</span>
<span id="L1788">                                ! If true use the bottom depth instead of the total water column thickness in</span>
<span id="L1789">                                ! the barotropic Coriolis term calculations.</span>
<span id="L1790">BEBT = 0.2                      !   [nondim] default = 0.1</span>
<span id="L1791">                                ! BEBT determines whether the barotropic time stepping uses the forward-backward</span>
<span id="L1792">                                ! time-stepping scheme or a backward Euler scheme. BEBT is valid in the range</span>
<span id="L1793">                                ! from 0 (for a forward-backward treatment of nonrotating gravity waves) to 1</span>
<span id="L1794">                                ! (for a backward Euler treatment). In practice, BEBT must be greater than about</span>
<span id="L1795">                                ! 0.05.</span>
<span id="L1796">DTBT = -0.95                    !   [s or nondim] default = -0.98</span>
<span id="L1797">                                ! The barotropic time step, in s. DTBT is only used with the split explicit time</span>
<span id="L1798">                                ! stepping. To set the time step automatically based the maximum stable value</span>
<span id="L1799">                                ! use 0, or a negative value gives the fraction of the stable value. Setting</span>
<span id="L1800">                                ! DTBT to 0 is the same as setting it to -0.98. The value of DTBT that will</span>
<span id="L1801">                                ! actually be used is an integer fraction of DT, rounding down.</span>
<span id="L1802">BT_USE_OLD_CORIOLIS_BRACKET_BUG = False !   [Boolean] default = False</span>
<span id="L1803">                                ! If True, use an order of operations that is not bitwise rotationally symmetric</span>
<span id="L1804">                                ! in the meridional Coriolis term of the barotropic solver.</span>
<span id="L1805">MASK_COASTAL_PRESSURE_FORCE = False !   [Boolean] default = False</span>
<span id="L1806">                                ! If true, use the land masks to zero out the diagnosed barotropic pressure</span>
<span id="L1807">                                ! gradient accelerations at coastal or land points.  This changes diagnostics</span>
<span id="L1808">                                ! and improves the reproducibility of certain debugging checksums, but it does</span>
<span id="L1809">                                ! not alter the solutions themselves.</span>
<span id="L1810"></span>
<span id="L1811">! === module MOM_mixed_layer_restrat ===</span>
<span id="L1812">MIXEDLAYER_RESTRAT = True       !   [Boolean] default = False</span>
<span id="L1813">                                ! If true, a density-gradient dependent re-stratifying flow is imposed in the</span>
<span id="L1814">                                ! mixed layer. Can be used in ALE mode without restriction but in layer mode can</span>
<span id="L1815">                                ! only be used if BULKMIXEDLAYER is true.</span>
<span id="L1816">MLE%</span>
<span id="L1817">USE_BODNER23 = False            !   [Boolean] default = False</span>
<span id="L1818">                                ! If true, use the Bodner et al., 2023, formulation of the re-stratifying</span>
<span id="L1819">                                ! mixed-layer restratification parameterization. This only works in ALE mode.</span>
<span id="L1820">%MLE</span>
<span id="L1821">FOX_KEMPER_ML_RESTRAT_COEF = 20.0 !   [nondim] default = 0.0</span>
<span id="L1822">                                ! A nondimensional coefficient that is proportional to the ratio of the</span>
<span id="L1823">                                ! deformation radius to the dominant lengthscale of the submesoscale mixed layer</span>
<span id="L1824">                                ! instabilities, times the minimum of the ratio of the mesoscale eddy kinetic</span>
<span id="L1825">                                ! energy to the large-scale geostrophic kinetic energy or 1 plus the square of</span>
<span id="L1826">                                ! the grid spacing over the deformation radius, as detailed by Fox-Kemper et al.</span>
<span id="L1827">                                ! (2011)</span>
<span id="L1828">USE_STANLEY_ML = False          !   [Boolean] default = False</span>
<span id="L1829">                                ! If true, turn on Stanley SGS T variance parameterization in ML restrat code.</span>
<span id="L1830">FOX_KEMPER_ML_RESTRAT_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L1831">                                ! As for FOX_KEMPER_ML_RESTRAT_COEF but used in a second application of the MLE</span>
<span id="L1832">                                ! restratification parameterization.</span>
<span id="L1833">MLE_FRONT_LENGTH = 0.0          !   [m] default = 0.0</span>
<span id="L1834">                                ! If non-zero, is the frontal-length scale used to calculate the upscaling of</span>
<span id="L1835">                                ! buoyancy gradients that is otherwise represented by the parameter</span>
<span id="L1836">                                ! FOX_KEMPER_ML_RESTRAT_COEF. If MLE_FRONT_LENGTH is non-zero, it is recommended</span>
<span id="L1837">                                ! to set FOX_KEMPER_ML_RESTRAT_COEF=1.0.</span>
<span id="L1838">MLE_FRONT_LENGTH_FROM_FILE = False !   [Boolean] default = False</span>
<span id="L1839">                                ! If true, the MLE front-length scale is read from a file.</span>
<span id="L1840">MLE_USE_PBL_MLD = False         !   [Boolean] default = False</span>
<span id="L1841">                                ! If true, the MLE parameterization will use the mixed-layer depth provided by</span>
<span id="L1842">                                ! the active PBL parameterization. If false, MLE will estimate a MLD based on a</span>
<span id="L1843">                                ! density difference with the surface using the parameter MLE_DENSITY_DIFF.</span>
<span id="L1844">MLE_MLD_DECAY_TIME = 0.0        !   [s] default = 0.0</span>
<span id="L1845">                                ! The time-scale for a running-mean filter applied to the mixed-layer depth used</span>
<span id="L1846">                                ! in the MLE restratification parameterization. When the MLD deepens below the</span>
<span id="L1847">                                ! current running-mean the running-mean is instantaneously set to the current</span>
<span id="L1848">                                ! MLD.</span>
<span id="L1849">MLE_MLD_DECAY_TIME2 = 0.0       !   [s] default = 0.0</span>
<span id="L1850">                                ! The time-scale for a running-mean filter applied to the filtered mixed-layer</span>
<span id="L1851">                                ! depth used in a second MLE restratification parameterization. When the MLD</span>
<span id="L1852">                                ! deepens below the current running-mean the running-mean is instantaneously set</span>
<span id="L1853">                                ! to the current MLD.</span>
<span id="L1854">MLE_DENSITY_DIFF = 0.03         !   [kg/m3] default = 0.03</span>
<span id="L1855">                                ! Density difference used to detect the mixed-layer depth used for the</span>
<span id="L1856">                                ! mixed-layer eddy parameterization by Fox-Kemper et al. (2011)</span>
<span id="L1857">MLE_TAIL_DH = 0.0               !   [nondim] default = 0.0</span>
<span id="L1858">                                ! Fraction by which to extend the mixed-layer restratification depth used for a</span>
<span id="L1859">                                ! smoother stream function at the base of the mixed-layer.</span>
<span id="L1860">MLE_MLD_STRETCH = 1.0           !   [nondim] default = 1.0</span>
<span id="L1861">                                ! A scaling coefficient for stretching/shrinking the MLD used in the MLE scheme.</span>
<span id="L1862">                                ! This simply multiplies MLD wherever used.</span>
<span id="L1863">KV_RESTRAT = 0.0                !   [m2 s-1] default = 0.0</span>
<span id="L1864">                                ! A small viscosity that sets a floor on the momentum mixing rate during</span>
<span id="L1865">                                ! restratification.  If this is positive, it will prevent some possible</span>
<span id="L1866">                                ! divisions by zero even if ustar, RESTRAT_USTAR_MIN, and f are all 0.</span>
<span id="L1867">RESTRAT_USTAR_MIN = 1.45842E-18 !   [m s-1] default = 1.45842E-18</span>
<span id="L1868">                                ! The minimum value of ustar that will be used by the mixed layer</span>
<span id="L1869">                                ! restratification module.  This can be tiny, but if this is greater than 0, it</span>
<span id="L1870">                                ! will prevent divisions by zero when f and KV_RESTRAT are zero.</span>
<span id="L1871"></span>
<span id="L1872">! === module MOM_diagnostics ===</span>
<span id="L1873">DIAG_EBT_MONO_N2_COLUMN_FRACTION = 0.0 !   [nondim] default = 0.0</span>
<span id="L1874">                                ! The lower fraction of water column over which N2 is limited as monotonic for</span>
<span id="L1875">                                ! the purposes of calculating the equivalent barotropic wave speed.</span>
<span id="L1876">DIAG_EBT_MONO_N2_DEPTH = -1.0   !   [m] default = -1.0</span>
<span id="L1877">                                ! The depth below which N2 is limited as monotonic for the purposes of</span>
<span id="L1878">                                ! calculating the equivalent barotropic wave speed.</span>
<span id="L1879">INTWAVE_REMAPPING_USE_OM4_SUBCELLS = True !   [Boolean] default = True</span>
<span id="L1880">                                ! If true, use the OM4 remapping-via-subcells algorithm for calculating EBT</span>
<span id="L1881">                                ! structure. See REMAPPING_USE_OM4_SUBCELLS for details. We recommend setting</span>
<span id="L1882">                                ! this option to false.</span>
<span id="L1883"></span>
<span id="L1884">! === module MOM_diabatic_driver ===</span>
<span id="L1885">! The following parameters are used for diabatic processes.</span>
<span id="L1886">USE_LEGACY_DIABATIC_DRIVER = False !   [Boolean] default = True</span>
<span id="L1887">                                ! If true, use a legacy version of the diabatic subroutine. This is temporary</span>
<span id="L1888">                                ! and is needed to avoid change in answers.</span>
<span id="L1889">ENERGETICS_SFC_PBL = True       !   [Boolean] default = False</span>
<span id="L1890">                                ! If true, use an implied energetics planetary boundary layer scheme to</span>
<span id="L1891">                                ! determine the diffusivity and viscosity in the surface boundary layer.</span>
<span id="L1892">EPBL_IS_ADDITIVE = True         !   [Boolean] default = True</span>
<span id="L1893">                                ! If true, the diffusivity from ePBL is added to all other diffusivities.</span>
<span id="L1894">                                ! Otherwise, the larger of kappa-shear and ePBL diffusivities are used.</span>
<span id="L1895">PRANDTL_EPBL = 1.0              !   [nondim] default = 1.0</span>
<span id="L1896">                                ! The Prandtl number used by ePBL to convert vertical diffusivities into</span>
<span id="L1897">                                ! viscosities.</span>
<span id="L1898">INTERNAL_TIDES = False          !   [Boolean] default = False</span>
<span id="L1899">                                ! If true, use the code that advances a separate set of equations for the</span>
<span id="L1900">                                ! internal tide energy density.</span>
<span id="L1901">MASSLESS_MATCH_TARGETS = True   !   [Boolean] default = True</span>
<span id="L1902">                                ! If true, the temperature and salinity of massless layers are kept consistent</span>
<span id="L1903">                                ! with their target densities. Otherwise the properties of massless layers</span>
<span id="L1904">                                ! evolve diffusively to match massive neighboring layers.</span>
<span id="L1905">AGGREGATE_FW_FORCING = True     !   [Boolean] default = True</span>
<span id="L1906">                                ! If true, the net incoming and outgoing fresh water fluxes are combined and</span>
<span id="L1907">                                ! applied as either incoming or outgoing depending on the sign of the net. If</span>
<span id="L1908">                                ! false, the net incoming fresh water flux is added to the model and thereafter</span>
<span id="L1909">                                ! the net outgoing is removed from the topmost non-vanished layers of the</span>
<span id="L1910">                                ! updated state.</span>
<span id="L1911">MIX_BOUNDARY_TRACERS = True     !   [Boolean] default = True</span>
<span id="L1912">                                ! If true, mix the passive tracers in massless layers at the bottom into the</span>
<span id="L1913">                                ! interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1914">MIX_BOUNDARY_TRACER_ALE = False !   [Boolean] default = False</span>
<span id="L1915">                                ! If true and in ALE mode, mix the passive tracers in massless layers at the</span>
<span id="L1916">                                ! bottom into the interior as though a diffusivity of KD_MIN_TR were operating.</span>
<span id="L1917">KD_MIN_TR = 2.0E-06             !   [m2 s-1] default = 2.0E-06</span>
<span id="L1918">                                ! A minimal diffusivity that should always be applied to tracers, especially in</span>
<span id="L1919">                                ! massless layers near the bottom. The default is 0.1*KD.</span>
<span id="L1920">KD_BBL_TR = 0.0                 !   [m2 s-1] default = 0.0</span>
<span id="L1921">                                ! A bottom boundary layer tracer diffusivity that will allow for explicitly</span>
<span id="L1922">                                ! specified bottom fluxes. The entrainment at the bottom is at least</span>
<span id="L1923">                                ! sqrt(Kd_BBL_tr*dt) over the same distance.</span>
<span id="L1924">TRACER_TRIDIAG = False          !   [Boolean] default = False</span>
<span id="L1925">                                ! If true, use the passive tracer tridiagonal solver for T and S</span>
<span id="L1926">MINIMUM_FORCING_DEPTH = 0.001   !   [m] default = 0.001</span>
<span id="L1927">                                ! The smallest depth over which forcing can be applied. This only takes effect</span>
<span id="L1928">                                ! when near-surface layers become thin relative to this scale, in which case the</span>
<span id="L1929">                                ! forcing tendencies scaled down by distributing the forcing over this depth</span>
<span id="L1930">                                ! scale.</span>
<span id="L1931">EVAP_CFL_LIMIT = 0.8            !   [nondim] default = 0.8</span>
<span id="L1932">                                ! The largest fraction of a layer than can be lost to forcing (e.g. evaporation,</span>
<span id="L1933">                                ! sea-ice formation) in one time-step. The unused mass loss is passed down</span>
<span id="L1934">                                ! through the column.</span>
<span id="L1935">MLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1936">                                ! The energy values used to compute MLDs.  If not set (or all set to 0.), the</span>
<span id="L1937">                                ! default will overwrite to 25., 2500., 250000.</span>
<span id="L1938">BMLD_EN_VALS = 25.0, 2500.0, 2.5E+05 !   [J/m2] default = 25.0, 2500.0, 2.5E+05</span>
<span id="L1939">                                ! The energy values used to compute Bottom MLDs.  If not set (or all set to 0.),</span>
<span id="L1940">                                ! the default will overwrite to 25., 2500., 250000.</span>
<span id="L1941">HREF_FOR_MLD = 0.0              !   [m] default = 0.0</span>
<span id="L1942">                                ! Reference depth used to calculate the potential density used to find the mixed</span>
<span id="L1943">                                ! layer depth based on a delta rho = 0.03 kg/m3.</span>
<span id="L1944">DIAG_MLD_DENSITY_DIFF = 0.1     !   [kg/m3] default = 0.1</span>
<span id="L1945">                                ! The density difference used to determine a diagnostic mixed layer depth,</span>
<span id="L1946">                                ! MLD_user, following the definition of Levitus 1982. The MLD is the depth at</span>
<span id="L1947">                                ! which the density is larger than the surface density by the specified amount.</span>
<span id="L1948">DIAG_DEPTH_SUBML_N2 = 50.0      !   [m] default = 50.0</span>
<span id="L1949">                                ! The distance over which to calculate a diagnostic of the stratification at the</span>
<span id="L1950">                                ! base of the mixed layer.</span>
<span id="L1951"></span>
<span id="L1952">! === module MOM_CVMix_KPP ===</span>
<span id="L1953">! This is the MOM wrapper to CVMix:KPP</span>
<span id="L1954">! See http://cvmix.github.io/</span>
<span id="L1955">USE_KPP = False                 !   [Boolean] default = False</span>
<span id="L1956">                                ! If true, turns on the [CVMix] KPP scheme of Large et al., 1994, to calculate</span>
<span id="L1957">                                ! diffusivities and non-local transport in the OBL.</span>
<span id="L1958"></span>
<span id="L1959">! === module MOM_CVMix_conv ===</span>
<span id="L1960">! Parameterization of enhanced mixing due to convection via CVMix</span>
<span id="L1961">USE_CVMix_CONVECTION = False    !   [Boolean] default = False</span>
<span id="L1962">                                ! If true, turns on the enhanced mixing due to convection via CVMix. This scheme</span>
<span id="L1963">                                ! increases diapycnal diffs./viscs. at statically unstable interfaces. Relevant</span>
<span id="L1964">                                ! parameters are contained in the CVMix_CONVECTION% parameter block.</span>
<span id="L1965"></span>
<span id="L1966">! === module MOM_geothermal ===</span>
<span id="L1967">GEOTHERMAL_SCALE = 0.001        !   [W m-2 or various] default = 0.0</span>
<span id="L1968">                                ! The constant geothermal heat flux, a rescaling factor for the heat flux read</span>
<span id="L1969">                                ! from GEOTHERMAL_FILE, or 0 to disable the geothermal heating.</span>
<span id="L1970">GEOTHERMAL_FILE = &quot;geothermal_heating_cm2g.nc&quot; ! default = &quot;&quot;</span>
<span id="L1971">                                ! The file from which the geothermal heating is to be read, or blank to use a</span>
<span id="L1972">                                ! constant heating rate.</span>
<span id="L1973">GEOTHERMAL_THICKNESS = 0.1      !   [m] default = 0.1</span>
<span id="L1974">                                ! The thickness over which to apply geothermal heating.</span>
<span id="L1975">GEOTHERMAL_VARNAME = &quot;geo_heat&quot; ! default = &quot;geo_heat&quot;</span>
<span id="L1976">                                ! The name of the geothermal heating variable in GEOTHERMAL_FILE.</span>
<span id="L1977"></span>
<span id="L1978">! === module MOM_set_diffusivity ===</span>
<span id="L1979">FLUX_RI_MAX = 0.2               !   [nondim] default = 0.2</span>
<span id="L1980">                                ! The flux Richardson number where the stratification is large enough that N2 &gt;</span>
<span id="L1981">                                ! omega2.  The full expression for the Flux Richardson number is usually</span>
<span id="L1982">                                ! FLUX_RI_MAX*N2/(N2+OMEGA2).</span>
<span id="L1983">SET_DIFF_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1984">                                ! The vintage of the order of arithmetic and expressions in the set diffusivity</span>
<span id="L1985">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L1986">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L1987">                                ! Values above 20250301 also use less confusing expressions to set the</span>
<span id="L1988">                                ! bottom-drag generated diffusivity when USE_LOTW_BBL_DIFFUSIVITY is false.</span>
<span id="L1989"></span>
<span id="L1990">! === module MOM_tidal_mixing ===</span>
<span id="L1991">! Vertical Tidal Mixing Parameterization</span>
<span id="L1992">USE_CVMix_TIDAL = False         !   [Boolean] default = False</span>
<span id="L1993">                                ! If true, turns on tidal mixing via CVMix</span>
<span id="L1994">INT_TIDE_DISSIPATION = True     !   [Boolean] default = False</span>
<span id="L1995">                                ! If true, use an internal tidal dissipation scheme to drive diapycnal mixing,</span>
<span id="L1996">                                ! along the lines of St. Laurent et al. (2002) and Simmons et al. (2004).</span>
<span id="L1997">TIDAL_MIXING_ANSWER_DATE = 99991231 ! default = 99991231</span>
<span id="L1998">                                ! The vintage of the order of arithmetic and expressions in the tidal mixing</span>
<span id="L1999">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L2000">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L2001">INT_TIDE_PROFILE = &quot;STLAURENT_02&quot; ! default = &quot;STLAURENT_02&quot;</span>
<span id="L2002">                                ! INT_TIDE_PROFILE selects the vertical profile of energy dissipation with</span>
<span id="L2003">                                ! INT_TIDE_DISSIPATION. Valid values are:</span>
<span id="L2004">                                !    STLAURENT_02 - Use the St. Laurent et al exponential</span>
<span id="L2005">                                !                   decay profile.</span>
<span id="L2006">                                !    POLZIN_09 - Use the Polzin WKB-stretched algebraic</span>
<span id="L2007">                                !                   decay profile.</span>
<span id="L2008">LEE_WAVE_DISSIPATION = False    !   [Boolean] default = False</span>
<span id="L2009">                                ! If true, use an lee wave driven dissipation scheme to drive diapycnal mixing,</span>
<span id="L2010">                                ! along the lines of Nikurashin (2010) and using the St. Laurent et al. (2002)</span>
<span id="L2011">                                ! and Simmons et al. (2004) vertical profile</span>
<span id="L2012">INT_TIDE_LOWMODE_DISSIPATION = False !   [Boolean] default = False</span>
<span id="L2013">                                ! If true, consider mixing due to breaking low modes that have been remotely</span>
<span id="L2014">                                ! generated; as with itidal drag on the barotropic tide, use an internal tidal</span>
<span id="L2015">                                ! dissipation scheme to drive diapycnal mixing, along the lines of St. Laurent</span>
<span id="L2016">                                ! et al. (2002) and Simmons et al. (2004).</span>
<span id="L2017">INT_TIDE_DECAY_SCALE = 300.3003003003003 !   [m] default = 500.0</span>
<span id="L2018">                                ! The decay scale away from the bottom for tidal TKE with the new coding when</span>
<span id="L2019">                                ! INT_TIDE_DISSIPATION is used.</span>
<span id="L2020">MU_ITIDES = 0.2                 !   [nondim] default = 0.2</span>
<span id="L2021">                                ! A dimensionless turbulent mixing efficiency used with INT_TIDE_DISSIPATION,</span>
<span id="L2022">                                ! often 0.2.</span>
<span id="L2023">GAMMA_ITIDES = 0.3333           !   [nondim] default = 0.3333</span>
<span id="L2024">                                ! The fraction of the internal tidal energy that is dissipated locally with</span>
<span id="L2025">                                ! INT_TIDE_DISSIPATION. THIS NAME COULD BE BETTER.</span>
<span id="L2026">MIN_ZBOT_ITIDES = 0.0           !   [m] default = 0.0</span>
<span id="L2027">                                ! Turn off internal tidal dissipation when the total ocean depth is less than</span>
<span id="L2028">                                ! this value.</span>
<span id="L2029">KAPPA_ITIDES = 6.28319E-04      !   [m-1] default = 6.283185307179586E-04</span>
<span id="L2030">                                ! A topographic wavenumber used with INT_TIDE_DISSIPATION. The default is 2pi/10</span>
<span id="L2031">                                ! km, as in St.Laurent et al. 2002.</span>
<span id="L2032">UTIDE = 0.0                     !   [m s-1] default = 0.0</span>
<span id="L2033">                                ! The constant tidal amplitude used with INT_TIDE_DISSIPATION.</span>
<span id="L2034">KAPPA_H2_FACTOR = 0.75          !   [nondim] default = 1.0</span>
<span id="L2035">                                ! A scaling factor for the roughness amplitude with INT_TIDE_DISSIPATION.</span>
<span id="L2036">TKE_ITIDE_MAX = 0.1             !   [W m-2] default = 1000.0</span>
<span id="L2037">                                ! The maximum internal tide energy source available to mix above the bottom</span>
<span id="L2038">                                ! boundary layer with INT_TIDE_DISSIPATION.</span>
<span id="L2039">READ_TIDEAMP = True             !   [Boolean] default = False</span>
<span id="L2040">                                ! If true, read a file (given by TIDEAMP_FILE) containing the tidal amplitude</span>
<span id="L2041">                                ! with INT_TIDE_DISSIPATION.</span>
<span id="L2042">TIDEAMP_FILE = &quot;tideamp.nc&quot;     ! default = &quot;tideamp.nc&quot;</span>
<span id="L2043">                                ! The path to the file containing the spatially varying tidal amplitudes with</span>
<span id="L2044">                                ! INT_TIDE_DISSIPATION.</span>
<span id="L2045">TIDEAMP_VARNAME = &quot;tideamp&quot;     ! default = &quot;tideamp&quot;</span>
<span id="L2046">                                ! The name of the tidal amplitude variable in the input file.</span>
<span id="L2047">H2_FILE = &quot;sgs_h2.nc&quot;           !</span>
<span id="L2048">                                ! The path to the file containing the sub-grid-scale topographic roughness</span>
<span id="L2049">                                ! amplitude with INT_TIDE_DISSIPATION.</span>
<span id="L2050">ROUGHNESS_VARNAME = &quot;h2&quot;        ! default = &quot;h2&quot;</span>
<span id="L2051">                                ! The name in the input file of the squared sub-grid-scale topographic roughness</span>
<span id="L2052">                                ! amplitude variable.</span>
<span id="L2053">FRACTIONAL_ROUGHNESS_MAX = 0.1  !   [nondim] default = 0.1</span>
<span id="L2054">                                ! The maximum topographic roughness amplitude as a fraction of the mean depth,</span>
<span id="L2055">                                ! or a negative value for no limitations on roughness.</span>
<span id="L2056">ML_RADIATION = False            !   [Boolean] default = False</span>
<span id="L2057">                                ! If true, allow a fraction of TKE available from wind work to penetrate below</span>
<span id="L2058">                                ! the base of the mixed layer with a vertical decay scale determined by the</span>
<span id="L2059">                                ! minimum of: (1) The depth of the mixed layer, (2) an Ekman length scale.</span>
<span id="L2060">BBL_EFFIC = 0.2                 !   [nondim] default = 0.2</span>
<span id="L2061">                                ! The efficiency with which the energy extracted by bottom drag drives BBL</span>
<span id="L2062">                                ! diffusion.  This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L2063">BBL_MIXING_MAX_DECAY = 200.0    !   [m] default = 200.0</span>
<span id="L2064">                                ! The maximum decay scale for the BBL diffusion, or 0 to allow the mixing to</span>
<span id="L2065">                                ! penetrate as far as stratification and rotation permit.  The default for now</span>
<span id="L2066">                                ! is 200 m. This is only used if BOTTOMDRAGLAW is true.</span>
<span id="L2067">BBL_MIXING_AS_MAX = False       !   [Boolean] default = True</span>
<span id="L2068">                                ! If true, take the maximum of the diffusivity from the BBL mixing and the other</span>
<span id="L2069">                                ! diffusivities. Otherwise, diffusivity from the BBL_mixing is simply added.</span>
<span id="L2070">USE_LOTW_BBL_DIFFUSIVITY = True !   [Boolean] default = False</span>
<span id="L2071">                                ! If true, uses a simple, imprecise but non-coordinate dependent, model of BBL</span>
<span id="L2072">                                ! mixing diffusivity based on Law of the Wall. Otherwise, uses the original BBL</span>
<span id="L2073">                                ! scheme.</span>
<span id="L2074">LOTW_BBL_USE_OMEGA = True       !   [Boolean] default = True</span>
<span id="L2075">                                ! If true, use the maximum of Omega and N for the TKE to diffusion calculation.</span>
<span id="L2076">                                ! Otherwise, N is N.</span>
<span id="L2077">VON_KARMAN_BBL = 0.41           !   [nondim] default = 0.41</span>
<span id="L2078">                                ! The value the von Karman constant as used in calculating the BBL diffusivity.</span>
<span id="L2079">LOTW_BBL_ANSWER_DATE = 20190101 ! default = 99991231</span>
<span id="L2080">                                ! The vintage of the order of arithmetic and expressions in the LOTW_BBL</span>
<span id="L2081">                                ! calculations.  Values below 20240630 recover the original answers, while</span>
<span id="L2082">                                ! higher values use more accurate expressions.  This only applies when</span>
<span id="L2083">                                ! USE_LOTW_BBL_DIFFUSIVITY is true.</span>
<span id="L2084">DZ_BBL_AVG_MIN = 0.0            !   [m] default = 0.0</span>
<span id="L2085">                                ! A minimal distance over which to average to determine the average bottom</span>
<span id="L2086">                                ! boundary layer density.</span>
<span id="L2087">SIMPLE_TKE_TO_KD = True         !   [Boolean] default = False</span>
<span id="L2088">                                ! If true, uses a simple estimate of Kd/TKE that will work for arbitrary</span>
<span id="L2089">                                ! vertical coordinates. If false, calculates Kd/TKE and bounds based on exact</span>
<span id="L2090">                                ! energetics for an isopycnal layer-formulation.</span>
<span id="L2091"></span>
<span id="L2092">! === module MOM_bkgnd_mixing ===</span>
<span id="L2093">! Adding static vertical background mixing coefficients</span>
<span id="L2094">KD = 2.0E-05                    !   [m2 s-1] default = 0.0</span>
<span id="L2095">                                ! The background diapycnal diffusivity of density in the interior. Zero or the</span>
<span id="L2096">                                ! molecular value, ~1e-7 m2 s-1, may be used.</span>
<span id="L2097">KD_MIN = 2.0E-06                !   [m2 s-1] default = 2.0E-07</span>
<span id="L2098">                                ! The minimum diapycnal diffusivity.</span>
<span id="L2099">BRYAN_LEWIS_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L2100">                                ! If true, use a Bryan &amp; Lewis (JGR 1979) like tanh profile of background</span>
<span id="L2101">                                ! diapycnal diffusivity with depth. This is done via CVMix.</span>
<span id="L2102">HORIZ_VARYING_BACKGROUND = False !   [Boolean] default = False</span>
<span id="L2103">                                ! If true, apply vertically uniform, latitude-dependent background diffusivity,</span>
<span id="L2104">                                ! as described in Danabasoglu et al., 2012</span>
<span id="L2105">PRANDTL_BKGND = 1.0             !   [nondim] default = 1.0</span>
<span id="L2106">                                ! Turbulent Prandtl number used to convert vertical background diffusivities</span>
<span id="L2107">                                ! into viscosities.</span>
<span id="L2108">HENYEY_IGW_BACKGROUND = True    !   [Boolean] default = False</span>
<span id="L2109">                                ! If true, use a latitude-dependent scaling for the near surface background</span>
<span id="L2110">                                ! diffusivity, as described in Harrison &amp; Hallberg, JPO 2008.</span>
<span id="L2111">HENYEY_N0_2OMEGA = 20.0         !   [nondim] default = 20.0</span>
<span id="L2112">                                ! The ratio of the typical Buoyancy frequency to twice the Earth&#x27;s rotation</span>
<span id="L2113">                                ! period, used with the Henyey scaling from the mixing.</span>
<span id="L2114">HENYEY_MAX_LAT = 95.0           !   [degN] default = 95.0</span>
<span id="L2115">                                ! A latitude poleward of which the Henyey profile is returned to the minimum</span>
<span id="L2116">                                ! diffusivity</span>
<span id="L2117">KD_TANH_LAT_FN = False          !   [Boolean] default = False</span>
<span id="L2118">                                ! If true, use a tanh dependence of Kd_sfc on latitude, like CM2.1/CM2M.  There</span>
<span id="L2119">                                ! is no physical justification for this form, and it can not be used with</span>
<span id="L2120">                                ! HENYEY_IGW_BACKGROUND.</span>
<span id="L2121">KD_MAX = 0.1                    !   [m2 s-1] default = -1.0</span>
<span id="L2122">                                ! The maximum permitted increment for the diapycnal diffusivity from TKE-based</span>
<span id="L2123">                                ! parameterizations, or a negative value for no limit.</span>
<span id="L2124">KD_ADD = 0.0                    !   [m2 s-1] default = 0.0</span>
<span id="L2125">                                ! A uniform diapycnal diffusivity that is added everywhere without any filtering</span>
<span id="L2126">                                ! or scaling.</span>
<span id="L2127">USER_CHANGE_DIFFUSIVITY = False !   [Boolean] default = False</span>
<span id="L2128">                                ! If true, call user-defined code to change the diffusivity.</span>
<span id="L2129">DISSIPATION_MIN = 0.0           !   [W m-3] default = 0.0</span>
<span id="L2130">                                ! The minimum dissipation by which to determine a lower bound of Kd (a floor).</span>
<span id="L2131">DISSIPATION_N0 = 0.0            !   [W m-3] default = 0.0</span>
<span id="L2132">                                ! The intercept when N=0 of the N-dependent expression used to set a minimum</span>
<span id="L2133">                                ! dissipation by which to determine a lower bound of Kd (a floor): A in eps_min</span>
<span id="L2134">                                ! = A + B*N.</span>
<span id="L2135">DISSIPATION_N1 = 0.0            !   [J m-3] default = 0.0</span>
<span id="L2136">                                ! The coefficient multiplying N, following Gargett, used to set a minimum</span>
<span id="L2137">                                ! dissipation by which to determine a lower bound of Kd (a floor): B in eps_min</span>
<span id="L2138">                                ! = A + B*N</span>
<span id="L2139">DISSIPATION_KD_MIN = 0.0        !   [m2 s-1] default = 0.0</span>
<span id="L2140">                                ! The minimum vertical diffusivity applied as a floor.</span>
<span id="L2141">DOUBLE_DIFFUSION = False        !   [Boolean] default = False</span>
<span id="L2142">                                ! If true, increase diffusivites for temperature or salinity based on the</span>
<span id="L2143">                                ! double-diffusive parameterization described in Large et al. (1994).</span>
<span id="L2144"></span>
<span id="L2145">! === module MOM_kappa_shear ===</span>
<span id="L2146">! Parameterization of shear-driven turbulence following Jackson, Hallberg and Legg, JPO 2008</span>
<span id="L2147">USE_JACKSON_PARAM = True        !   [Boolean] default = False</span>
<span id="L2148">                                ! If true, use the Jackson-Hallberg-Legg (JPO 2008) shear mixing</span>
<span id="L2149">                                ! parameterization.</span>
<span id="L2150">VERTEX_SHEAR = False            !   [Boolean] default = False</span>
<span id="L2151">                                ! If true, do the calculations of the shear-driven mixing at the cell vertices</span>
<span id="L2152">                                ! (i.e., the vorticity points).</span>
<span id="L2153">VERTEX_SHEAR_THICKNESS_MEAN = False !   [Boolean] default = False</span>
<span id="L2154">                                ! If true, apply thickness weighting to horizontal averagings of diffusivity to</span>
<span id="L2155">                                ! tracer points in the kappa shear solver.</span>
<span id="L2156">RINO_CRIT = 0.25                !   [nondim] default = 0.25</span>
<span id="L2157">                                ! The critical Richardson number for shear mixing.</span>
<span id="L2158">SHEARMIX_RATE = 0.089           !   [nondim] default = 0.089</span>
<span id="L2159">                                ! A nondimensional rate scale for shear-driven entrainment. Jackson et al find</span>
<span id="L2160">                                ! values in the range of 0.085-0.089.</span>
<span id="L2161">MAX_RINO_IT = 25                !   [nondim] default = 50</span>
<span id="L2162">                                ! The maximum number of iterations that may be used to estimate the Richardson</span>
<span id="L2163">                                ! number driven mixing.</span>
<span id="L2164">KD_KAPPA_SHEAR_0 = 2.0E-05      !   [m2 s-1] default = 2.0E-05</span>
<span id="L2165">                                ! The background diffusivity that is used to smooth the density and shear</span>
<span id="L2166">                                ! profiles before solving for the diffusivities.  The default is the greater of</span>
<span id="L2167">                                ! KD and 1e-7 m2 s-1.</span>
<span id="L2168">KD_SEED_KAPPA_SHEAR = 1.0       !   [m2 s-1] default = 1.0</span>
<span id="L2169">                                ! A moderately large seed value of diapycnal diffusivity that is used as a</span>
<span id="L2170">                                ! starting turbulent diffusivity in the iterations to find an energetically</span>
<span id="L2171">                                ! constrained solution for the shear-driven diffusivity.</span>
<span id="L2172">KD_TRUNC_KAPPA_SHEAR = 2.0E-07  !   [m2 s-1] default = 2.0E-07</span>
<span id="L2173">                                ! The value of shear-driven diffusivity that is considered negligible and is</span>
<span id="L2174">                                ! rounded down to 0. The default is 1% of KD_KAPPA_SHEAR_0.</span>
<span id="L2175">FRI_CURVATURE = -0.97           !   [nondim] default = -0.97</span>
<span id="L2176">                                ! The nondimensional curvature of the function of the Richardson number in the</span>
<span id="L2177">                                ! kappa source term in the Jackson et al. scheme.</span>
<span id="L2178">TKE_N_DECAY_CONST = 0.24        !   [nondim] default = 0.24</span>
<span id="L2179">                                ! The coefficient for the decay of TKE due to stratification (i.e. proportional</span>
<span id="L2180">                                ! to N*tke). The values found by Jackson et al. are 0.24-0.28.</span>
<span id="L2181">TKE_SHEAR_DECAY_CONST = 0.14    !   [nondim] default = 0.14</span>
<span id="L2182">                                ! The coefficient for the decay of TKE due to shear (i.e. proportional to</span>
<span id="L2183">                                ! |S|*tke). The values found by Jackson et al. are 0.14-0.12.</span>
<span id="L2184">KAPPA_BUOY_SCALE_COEF = 0.82    !   [nondim] default = 0.82</span>
<span id="L2185">                                ! The coefficient for the buoyancy length scale in the kappa equation.  The</span>
<span id="L2186">                                ! values found by Jackson et al. are in the range of 0.81-0.86.</span>
<span id="L2187">KAPPA_N_OVER_S_SCALE_COEF2 = 0.0 !   [nondim] default = 0.0</span>
<span id="L2188">                                ! The square of the ratio of the coefficients of the buoyancy and shear scales</span>
<span id="L2189">                                ! in the diffusivity equation, Set this to 0 (the default) to eliminate the</span>
<span id="L2190">                                ! shear scale. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L2191">LZ_RESCALE = 1.0                !   [nondim] default = 1.0</span>
<span id="L2192">                                ! A coefficient to rescale the distance to the nearest solid boundary. This</span>
<span id="L2193">                                ! adjustment is to account for regions where 3 dimensional turbulence prevents</span>
<span id="L2194">                                ! the growth of shear instabilies [nondim].</span>
<span id="L2195">KAPPA_SHEAR_TOL_ERR = 0.1       !   [nondim] default = 0.1</span>
<span id="L2196">                                ! The fractional error in kappa that is tolerated. Iteration stops when changes</span>
<span id="L2197">                                ! between subsequent iterations are smaller than this everywhere in a column.</span>
<span id="L2198">                                ! The peak diffusivities usually converge most rapidly, and have much smaller</span>
<span id="L2199">                                ! errors than this.</span>
<span id="L2200">TKE_BACKGROUND = 0.0            !   [m2 s-2] default = 0.0</span>
<span id="L2201">                                ! A background level of TKE used in the first iteration of the kappa equation.</span>
<span id="L2202">                                ! TKE_BACKGROUND could be 0.</span>
<span id="L2203">KAPPA_SHEAR_ELIM_MASSLESS = True !   [Boolean] default = True</span>
<span id="L2204">                                ! If true, massless layers are merged with neighboring massive layers in this</span>
<span id="L2205">                                ! calculation.  The default is true and I can think of no good reason why it</span>
<span id="L2206">                                ! should be false. This is only used if USE_JACKSON_PARAM is true.</span>
<span id="L2207">MAX_KAPPA_SHEAR_IT = 13         ! default = 13</span>
<span id="L2208">                                ! The maximum number of iterations that may be used to estimate the</span>
<span id="L2209">                                ! time-averaged diffusivity.</span>
<span id="L2210">PRANDTL_TURB = 1.0              !   [nondim] default = 1.0</span>
<span id="L2211">                                ! The turbulent Prandtl number applied to shear instability.</span>
<span id="L2212">KAPPA_SHEAR_MAX_KAP_SRC_CHG = 10.0 !   [nondim] default = 10.0</span>
<span id="L2213">                                ! The maximum permitted increase in the kappa source within an iteration</span>
<span id="L2214">                                ! relative to the local source; this must be greater than 1.  The lower limit</span>
<span id="L2215">                                ! for the permitted fractional decrease is (1 - 0.5/kappa_src_max_chg).  These</span>
<span id="L2216">                                ! limits could perhaps be made dynamic with an improved iterative solver.</span>
<span id="L2217">KAPPA_SHEAR_ITER_BUG = False    !   [Boolean] default = False</span>
<span id="L2218">                                ! If true, use an older, dimensionally inconsistent estimate of the derivative</span>
<span id="L2219">                                ! of diffusivity with energy in the Newton&#x27;s method iteration.  The bug causes</span>
<span id="L2220">                                ! undercorrections when dz &gt; 1 m.</span>
<span id="L2221">KAPPA_SHEAR_ALL_LAYER_TKE_BUG = False !   [Boolean] default = False</span>
<span id="L2222">                                ! If true, report back the latest estimate of TKE instead of the time average</span>
<span id="L2223">                                ! TKE when there is mass in all layers.  Otherwise always report the time</span>
<span id="L2224">                                ! averaged TKE, as is currently done when there are some massless layers.</span>
<span id="L2225">USE_RESTRICTIVE_TOLERANCE_CHECK = False !   [Boolean] default = False</span>
<span id="L2226">                                ! If true, uses the more restrictive tolerance check to determine if a timestep</span>
<span id="L2227">                                ! is acceptable for the KS_it outer iteration loop.  False uses the original</span>
<span id="L2228">                                ! less restrictive check.</span>
<span id="L2229"></span>
<span id="L2230">! === module MOM_CVMix_shear ===</span>
<span id="L2231">! Parameterization of shear-driven turbulence via CVMix (various options)</span>
<span id="L2232">USE_LMD94 = False               !   [Boolean] default = False</span>
<span id="L2233">                                ! If true, use the Large-McWilliams-Doney (JGR 1994) shear mixing</span>
<span id="L2234">                                ! parameterization.</span>
<span id="L2235">USE_PP81 = False                !   [Boolean] default = False</span>
<span id="L2236">                                ! If true, use the Pacanowski and Philander (JPO 1981) shear mixing</span>
<span id="L2237">                                ! parameterization.</span>
<span id="L2238"></span>
<span id="L2239">! === module MOM_CVMix_ddiff ===</span>
<span id="L2240">! Parameterization of mixing due to double diffusion processes via CVMix</span>
<span id="L2241">USE_CVMIX_DDIFF = False         !   [Boolean] default = False</span>
<span id="L2242">                                ! If true, turns on double diffusive processes via CVMix. Note that double</span>
<span id="L2243">                                ! diffusive processes on viscosity are ignored in CVMix, see</span>
<span id="L2244">                                ! http://cvmix.github.io/ for justification.</span>
<span id="L2245"></span>
<span id="L2246">! === module MOM_diabatic_aux ===</span>
<span id="L2247">! The following parameters are used for auxiliary diabatic processes.</span>
<span id="L2248">RECLAIM_FRAZIL = True           !   [Boolean] default = True</span>
<span id="L2249">                                ! If true, try to use any frazil heat deficit to cool any overlying layers down</span>
<span id="L2250">                                ! to the freezing point, thereby avoiding the creation of thin ice when the SST</span>
<span id="L2251">                                ! is above the freezing point.</span>
<span id="L2252">SALT_EXTRACTION_LIMIT = 0.9999  !   [nondim] default = 0.9999</span>
<span id="L2253">                                ! An upper limit on the fraction of the salt in a layer that can be lost to the</span>
<span id="L2254">                                ! net surface salt fluxes within a timestep.</span>
<span id="L2255">PRESSURE_DEPENDENT_FRAZIL = False !   [Boolean] default = False</span>
<span id="L2256">                                ! If true, use a pressure dependent freezing temperature when making frazil. The</span>
<span id="L2257">                                ! default is false, which will be faster but is inappropriate with ice-shelf</span>
<span id="L2258">                                ! cavities.</span>
<span id="L2259">IGNORE_FLUXES_OVER_LAND = False !   [Boolean] default = False</span>
<span id="L2260">                                ! If true, the model does not check if fluxes are being applied over land</span>
<span id="L2261">                                ! points. This is needed when the ocean is coupled with ice shelves and sea ice,</span>
<span id="L2262">                                ! since the sea ice mask needs to be different than the ocean mask to avoid sea</span>
<span id="L2263">                                ! ice formation under ice shelves. This flag only works when use_ePBL = True.</span>
<span id="L2264">DO_RIVERMIX = False             !   [Boolean] default = False</span>
<span id="L2265">                                ! If true, apply additional mixing wherever there is runoff, so that it is mixed</span>
<span id="L2266">                                ! down to RIVERMIX_DEPTH if the ocean is that deep.</span>
<span id="L2267">USE_RIVER_HEAT_CONTENT = False  !   [Boolean] default = False</span>
<span id="L2268">                                ! If true, use the fluxes%runoff_Hflx field to set the heat carried by runoff,</span>
<span id="L2269">                                ! instead of using SST*CP*liq_runoff.</span>
<span id="L2270">USE_CALVING_HEAT_CONTENT = False !   [Boolean] default = False</span>
<span id="L2271">                                ! If true, use the fluxes%calving_Hflx field to set the heat carried by runoff,</span>
<span id="L2272">                                ! instead of using SST*CP*froz_runoff.</span>
<span id="L2273">DO_BRINE_PLUME = False          !   [Boolean] default = False</span>
<span id="L2274">                                ! If true, use a brine plume parameterization from Nguyen et al., 2009.</span>
<span id="L2275">VAR_PEN_SW = True               !   [Boolean] default = False</span>
<span id="L2276">                                ! If true, use one of the CHL_A schemes specified by OPACITY_SCHEME to determine</span>
<span id="L2277">                                ! the e-folding depth of incoming short wave radiation.</span>
<span id="L2278">CHL_FROM_FILE = True            !   [Boolean] default = True</span>
<span id="L2279">                                ! If true, chl_a is read from a file.</span>
<span id="L2280">CHL_FILE = &quot;seawifs_1998-2006_GOLD_smoothed_2X.nc&quot; !</span>
<span id="L2281">                                ! CHL_FILE is the file containing chl_a concentrations in the variable CHL_A. It</span>
<span id="L2282">                                ! is used when VAR_PEN_SW and CHL_FROM_FILE are true.</span>
<span id="L2283">CHL_VARNAME = &quot;CHL_A&quot;           ! default = &quot;CHL_A&quot;</span>
<span id="L2284">                                ! Name of CHL_A variable in CHL_FILE.</span>
<span id="L2285"></span>
<span id="L2286">! === module MOM_energetic_PBL ===</span>
<span id="L2287">ML_OMEGA_FRAC = 0.0             !   [nondim] default = 0.0</span>
<span id="L2288">                                ! When setting the decay scale for turbulence, use this fraction of the absolute</span>
<span id="L2289">                                ! rotation rate blended with the local value of f, as sqrt((1-of)*f^2 +</span>
<span id="L2290">                                ! of*4*omega^2).</span>
<span id="L2291">EKMAN_SCALE_COEF = 1.0          !   [nondim] default = 1.0</span>
<span id="L2292">                                ! A nondimensional scaling factor controlling the inhibition of the diffusive</span>
<span id="L2293">                                ! length scale by rotation. Making this larger decreases the PBL diffusivity.</span>
<span id="L2294">EPBL_ANSWER_DATE = 20231231     ! default = 99991231</span>
<span id="L2295">                                ! The vintage of the order of arithmetic and expressions in the energetic PBL</span>
<span id="L2296">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L2297">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L2298">                                ! Values below 20240101 use A**(1./3.) to estimate the cube root of A in several</span>
<span id="L2299">                                ! expressions, while higher values use the integer root function cuberoot(A) and</span>
<span id="L2300">                                ! therefore can work with scaled variables.</span>
<span id="L2301">EPBL_ORIGINAL_PE_CALC = True    !   [Boolean] default = True</span>
<span id="L2302">                                ! If true, the ePBL code uses the original form of the potential energy change</span>
<span id="L2303">                                ! code.  Otherwise, the newer version that can work with successive increments</span>
<span id="L2304">                                ! to the diffusivity in upward or downward passes is used.</span>
<span id="L2305">MKE_TO_TKE_EFFIC = 0.0          !   [nondim] default = 0.0</span>
<span id="L2306">                                ! The efficiency with which mean kinetic energy released by mechanically forced</span>
<span id="L2307">                                ! entrainment of the mixed layer is converted to turbulent kinetic energy.</span>
<span id="L2308">TKE_DECAY = 2.5                 !   [nondim] default = 2.5</span>
<span id="L2309">                                ! TKE_DECAY relates the vertical rate of decay of the TKE available for</span>
<span id="L2310">                                ! mechanical entrainment to the natural Ekman depth.</span>
<span id="L2311">DIRECT_EPBL_MIXING_CALC = False !   [Boolean] default = False</span>
<span id="L2312">                                ! If true and there is no conversion from mean kinetic energy to ePBL turbulent</span>
<span id="L2313">                                ! kinetic energy, use a direct calculation of the diffusivity that is supported</span>
<span id="L2314">                                ! by a given energy input instead of the more general but slower iterative</span>
<span id="L2315">                                ! solver.</span>
<span id="L2316">EPBL_MSTAR_SCHEME = &quot;CONSTANT&quot;  ! default = &quot;CONSTANT&quot;</span>
<span id="L2317">                                ! EPBL_MSTAR_SCHEME selects the method for setting mstar.  Valid values are:</span>
<span id="L2318">                                !    CONSTANT   - Use a fixed mstar given by MSTAR</span>
<span id="L2319">                                !    OM4        - Use L_Ekman/L_Obukhov in the stabilizing limit, as in OM4</span>
<span id="L2320">                                !    REICHL_H18 - Use the scheme documented in Reichl &amp; Hallberg, 2018.</span>
<span id="L2321">MSTAR = 1.2                     !   [nondim] default = 1.2</span>
<span id="L2322">                                ! The ratio of the friction velocity cubed to the TKE input to the surface</span>
<span id="L2323">                                ! boundary layer.  This option is used if EPBL_MSTAR_SCHEME = CONSTANT.</span>
<span id="L2324">EPBL_BBL_USE_MSTAR = False      !   [nondim] default = False</span>
<span id="L2325">                                ! A logical to use mstar in the calculation of TKE in the ePBL BBL scheme</span>
<span id="L2326">NSTAR = 0.2                     !   [nondim] default = 0.2</span>
<span id="L2327">                                ! The portion of the buoyant potential energy imparted by surface fluxes that is</span>
<span id="L2328">                                ! available to drive entrainment at the base of mixed layer when that energy is</span>
<span id="L2329">                                ! positive.</span>
<span id="L2330">MSTAR_CONV_ADJ = 0.0            !   [nondim] default = 0.0</span>
<span id="L2331">                                ! Coefficient used for reducing mstar during convection due to reduction of</span>
<span id="L2332">                                ! stable density gradient.</span>
<span id="L2333">USE_MLD_ITERATION = False       !   [Boolean] default = True</span>
<span id="L2334">                                ! A logical that specifies whether or not to use the distance to the bottom of</span>
<span id="L2335">                                ! the actively turbulent boundary layer to help set the EPBL length scale.</span>
<span id="L2336">EPBL_TRANSITION_SCALE = 0.1     !   [nondim] default = 0.1</span>
<span id="L2337">                                ! A scale for the mixing length in the transition layer at the edge of the</span>
<span id="L2338">                                ! boundary layer as a fraction of the boundary layer thickness.</span>
<span id="L2339">EPBL_MIN_MIX_LEN = 0.0          !   [meter] default = 0.0</span>
<span id="L2340">                                ! The minimum mixing length scale that will be used by ePBL.  The default (0)</span>
<span id="L2341">                                ! does not set a minimum.</span>
<span id="L2342">MIX_LEN_EXPONENT = 2.0          !   [nondim] default = 2.0</span>
<span id="L2343">                                ! The exponent applied to the ratio of the distance to the MLD and the MLD depth</span>
<span id="L2344">                                ! which determines the shape of the mixing length. This is only used if</span>
<span id="L2345">                                ! USE_MLD_ITERATION is True.</span>
<span id="L2346">EPBL_VEL_SCALE_SCHEME = &quot;CUBE_ROOT_TKE&quot; ! default = &quot;CUBE_ROOT_TKE&quot;</span>
<span id="L2347">                                ! Selects the method for translating TKE into turbulent velocities. Valid values</span>
<span id="L2348">                                ! are:</span>
<span id="L2349">                                !    CUBE_ROOT_TKE  - A constant times the cube root of remaining TKE.</span>
<span id="L2350">                                !    REICHL_H18 - Use the scheme based on a combination of w* and v* as</span>
<span id="L2351">                                !                 documented in Reichl &amp; Hallberg, 2018.</span>
<span id="L2352">WSTAR_USTAR_COEF = 1.0          !   [nondim] default = 1.0</span>
<span id="L2353">                                ! A ratio relating the efficiency with which convectively released energy is</span>
<span id="L2354">                                ! converted to a turbulent velocity, relative to mechanically forced TKE. Making</span>
<span id="L2355">                                ! this larger increases the BL diffusivity</span>
<span id="L2356">EPBL_VEL_SCALE_FACTOR = 1.0     !   [nondim] default = 1.0</span>
<span id="L2357">                                ! An overall nondimensional scaling factor for wT. Making this larger increases</span>
<span id="L2358">                                ! the PBL diffusivity.</span>
<span id="L2359">VSTAR_SURF_FAC = 1.2            !   [nondim] default = 1.2</span>
<span id="L2360">                                ! The proportionality times ustar to set vstar at the surface.</span>
<span id="L2361">EPBL_BBL_EFFIC = 0.0            !   [nondim] default = 0.0</span>
<span id="L2362">                                ! The efficiency of bottom boundary layer mixing via ePBL.  Setting this to a</span>
<span id="L2363">                                ! value that is greater than 0 to enable bottom boundary layer mixing from EPBL.</span>
<span id="L2364">EPBL_BBL_TIDAL_EFFIC = 0.0      !   [nondim] default = 0.0</span>
<span id="L2365">                                ! The efficiency of bottom boundary layer mixing via ePBL driven by the bottom</span>
<span id="L2366">                                ! drag dissipation of tides, as provided in fluxes%BBL_tidal_dis.</span>
<span id="L2367">USE_LA_LI2016 = False           !   [Boolean] default = False</span>
<span id="L2368">                                ! A logical to use the Li et al. 2016 (submitted) formula to determine the</span>
<span id="L2369">                                ! Langmuir number.</span>
<span id="L2370">EPBL_LT = False                 !   [Boolean] default = False</span>
<span id="L2371">                                ! A logical to use a LT parameterization.</span>
<span id="L2372">EPBL_EQD_DIFFUSIVITY_SHAPE = False !   [nondim] default = False</span>
<span id="L2373">                                ! Logical flag for activating ML equation for shape function that uses forcing</span>
<span id="L2374">                                ! to change its structure.</span>
<span id="L2375">EPBL_EQD_DIFFUSIVITY_VELOCITY = False !   [nondim] default = False</span>
<span id="L2376">                                ! Logical flag for activating ML equation discovery for velocity scale</span>
<span id="L2377">EPBL_EQD_DIFFUSIVITY_VELOCITY_H = False !   [nondim] default = False</span>
<span id="L2378">                                ! Logical flag for activating ML equation discovery for velocity scale with h as</span>
<span id="L2379">                                ! input</span>
<span id="L2380">EPBL_OPTIONS_DIFF = 0           ! default = 0</span>
<span id="L2381">                                ! If positive, this is a coded integer indicating a pair of settings whose</span>
<span id="L2382">                                ! differences are diagnosed in a passive diagnostic mode  via extra calls to</span>
<span id="L2383">                                ! ePBL_column.  If this is 0 or negative no extra calls occur.</span>
<span id="L2384">!EPBL_USTAR_MIN = 1.45842E-18   !   [m s-1]</span>
<span id="L2385">                                ! The (tiny) minimum friction velocity used within the ePBL code, derived from</span>
<span id="L2386">                                ! OMEGA and ANGSTROM.</span>
<span id="L2387"></span>
<span id="L2388">! === module MOM_regularize_layers ===</span>
<span id="L2389">REGULARIZE_SURFACE_LAYERS = False !   [Boolean] default = False</span>
<span id="L2390">                                ! If defined, vertically restructure the near-surface layers when they have too</span>
<span id="L2391">                                ! much lateral variations to allow for sensible lateral barotropic transports.</span>
<span id="L2392"></span>
<span id="L2393">! === module MOM_opacity ===</span>
<span id="L2394">OPACITY_SCHEME = &quot;MANIZZA_05&quot;   ! default = &quot;MANIZZA_05&quot;</span>
<span id="L2395">                                ! This character string specifies how chlorophyll concentrations are translated</span>
<span id="L2396">                                ! into opacities. Currently valid options include:</span>
<span id="L2397">                                !        MANIZZA_05 - Use Manizza et al., GRL, 2005.</span>
<span id="L2398">                                !        MOREL_88 - Use Morel, JGR, 1988.</span>
<span id="L2399">                                !        OHLMANN_03 - Use Ohlmann, J Clim, 2003. (only use if dz(1)&gt;2.0m)</span>
<span id="L2400">BLUE_FRAC_SW = 0.5              !   [nondim] default = 0.5</span>
<span id="L2401">                                ! The fraction of the penetrating shortwave radiation that is in the blue band.</span>
<span id="L2402">PEN_SW_NBANDS = 3               ! default = 1</span>
<span id="L2403">                                ! The number of bands of penetrating shortwave radiation.</span>
<span id="L2404">OPTICS_ANSWER_DATE = 99991231   ! default = 99991231</span>
<span id="L2405">                                ! The vintage of the order of arithmetic and expressions in the optics</span>
<span id="L2406">                                ! calculations.  Values below 20190101 recover the answers from the end of 2018,</span>
<span id="L2407">                                ! while higher values use updated and more robust forms of the same expressions.</span>
<span id="L2408">PEN_SW_FLUX_ABSORB = 2.5E-11    !   [degC m s-1] default = 2.5E-11</span>
<span id="L2409">                                ! A minimum remaining shortwave heating rate that will be simply absorbed in the</span>
<span id="L2410">                                ! next sufficiently thick layers for computational efficiency, instead of</span>
<span id="L2411">                                ! continuing to penetrate.  The default, 2.5e-11 degC m s-1, is about 1e-4 W m-2</span>
<span id="L2412">                                ! or 0.08 degC m century-1, but 0 is also a valid value.</span>
<span id="L2413">PEN_SW_ABSORB_MINTHICK = 1.0    !   [m] default = 1.0</span>
<span id="L2414">                                ! A thickness that is used to absorb the remaining penetrating shortwave heat</span>
<span id="L2415">                                ! flux when it drops below PEN_SW_FLUX_ABSORB.</span>
<span id="L2416">OPACITY_VALUES_MANIZZA = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0 !   [m-1] default = 0.0232, 0.074, 0.225, 0.037, 2.86, 0.0</span>
<span id="L2417">                                ! Pairs of opacity coefficients for blue, red and near-infrared radiation with</span>
<span id="L2418">                                ! parameterizations following the functional form from Manizza et al., GRL 2005,</span>
<span id="L2419">                                ! namely in the form opacity = coef_1 + coef_2 * chl**pow for each band.</span>
<span id="L2420">                                ! Although coefficients are set for 3 bands, more or less bands may actually be</span>
<span id="L2421">                                ! used, with extra bands following the same properties as band 3.</span>
<span id="L2422">CHOROPHYLL_POWER_MANIZZA = 0.674, 0.629, 0.0 !   [nondim] default = 0.674, 0.629, 0.0</span>
<span id="L2423">                                ! Powers of chlorophyll for blue, red and near-infrared radiation bands in</span>
<span id="L2424">                                ! expressions for opacity of the form opacity = coef_1 + coef_2 * chl**pow.</span>
<span id="L2425">OPACITY_BAND_WAVELENGTHS = 0.0, 550.0, 700.0, 2800.0 !   [nm] default = 0.0, 550.0, 700.0, 2800.0</span>
<span id="L2426">                                ! The bounding wavelengths for the various bands of shortwave radiation, with</span>
<span id="L2427">                                ! defaults that depend on the setting for OPACITY_SCHEME.</span>
<span id="L2428">OPACITY_LAND_VALUE = 10.0       !   [m-1] default = 10.0</span>
<span id="L2429">                                ! The value to use for opacity over land. The default is 10 m-1 - a value for</span>
<span id="L2430">                                ! muddy water.</span>
<span id="L2431"></span>
<span id="L2432">! === module MOM_tracer_advect ===</span>
<span id="L2433">TRACER_ADVECTION_SCHEME = &quot;PPM:H3&quot; ! default = &quot;PLM&quot;</span>
<span id="L2434">                                ! The horizontal transport scheme for tracers:</span>
<span id="L2435">                                !   PLM    - Piecewise Linear Method</span>
<span id="L2436">                                !   PPM:H3 - Piecewise Parabolic Method (Huyhn 3rd order)</span>
<span id="L2437">                                !   PPM    - Piecewise Parabolic Method (Colella-Woodward)</span>
<span id="L2438">USE_HUYNH_STENCIL_BUG = False   !   [Boolean] default = False</span>
<span id="L2439">                                ! If true, use a stencil width of 2 in PPM:H3 tracer advection. This is</span>
<span id="L2440">                                ! incorrect and will produce regressions in certain configurations, but may be</span>
<span id="L2441">                                ! required to reproduce results in legacy simulations.</span>
<span id="L2442"></span>
<span id="L2443">! === module MOM_tracer_hor_diff ===</span>
<span id="L2444">KHTR = 600.0                    !   [m2 s-1] default = 0.0</span>
<span id="L2445">                                ! The background along-isopycnal tracer diffusivity.</span>
<span id="L2446">KHTR_MIN = 50.0                 !   [m2 s-1] default = 0.0</span>
<span id="L2447">                                ! The minimum along-isopycnal tracer diffusivity.</span>
<span id="L2448">FULL_DEPTH_KHTR_MIN = False     !   [Boolean] default = False</span>
<span id="L2449">                                ! If true, KHTR_MIN is enforced throughout the whole water column. Otherwise,</span>
<span id="L2450">                                ! KHTR_MIN is only enforced at the surface. This parameter is only available</span>
<span id="L2451">                                ! when KHTR_USE_EBT_STRUCT=True and KHTR_MIN&gt;0.</span>
<span id="L2452">KHTR_MAX = 900.0                !   [m2 s-1] default = 0.0</span>
<span id="L2453">                                ! The maximum along-isopycnal tracer diffusivity. Set to a positive value to</span>
<span id="L2454">                                ! activate.</span>
<span id="L2455">KHTR_PASSIVITY_COEFF = 0.0      !   [nondim] default = 0.0</span>
<span id="L2456">                                ! The coefficient that scales deformation radius over grid-spacing in passivity,</span>
<span id="L2457">                                ! where passivity is the ratio between along isopycnal mixing of tracers to</span>
<span id="L2458">                                ! thickness mixing. A non-zero value enables this parameterization.</span>
<span id="L2459">KHTR_PASSIVITY_MIN = 0.5        !   [nondim] default = 0.5</span>
<span id="L2460">                                ! The minimum passivity which is the ratio between along isopycnal mixing of</span>
<span id="L2461">                                ! tracers to thickness mixing.</span>
<span id="L2462">DIFFUSE_ML_TO_INTERIOR = False  !   [Boolean] default = False</span>
<span id="L2463">                                ! If true, enable epipycnal mixing between the surface boundary layer and the</span>
<span id="L2464">                                ! interior.</span>
<span id="L2465">CHECK_DIFFUSIVE_CFL = False     !   [Boolean] default = False</span>
<span id="L2466">                                ! If true, use enough iterations the diffusion to ensure that the diffusive</span>
<span id="L2467">                                ! equivalent of the CFL limit is not violated.  If false, always use the greater</span>
<span id="L2468">                                ! of 1 or MAX_TR_DIFFUSION_CFL iteration.</span>
<span id="L2469">MAX_TR_DIFFUSION_CFL = -1.0     !   [nondim] default = -1.0</span>
<span id="L2470">                                ! If positive, locally limit the along-isopycnal tracer diffusivity to keep the</span>
<span id="L2471">                                ! diffusive CFL locally at or below this value.  The number of diffusive</span>
<span id="L2472">                                ! iterations is often this value or the next greater integer.</span>
<span id="L2473">RECALC_NEUTRAL_SURF = False     !   [Boolean] default = False</span>
<span id="L2474">                                ! If true, then recalculate the neutral surfaces if the</span>
<span id="L2475">                                ! diffusive CFL is exceeded. If false, assume that the</span>
<span id="L2476">                                ! positions of the surfaces do not change</span>
<span id="L2477"></span>
<span id="L2478">! === module MOM_neutral_diffusion ===</span>
<span id="L2479">! This module implements neutral diffusion of tracers</span>
<span id="L2480">USE_NEUTRAL_DIFFUSION = True    !   [Boolean] default = False</span>
<span id="L2481">                                ! If true, enables the neutral diffusion module.</span>
<span id="L2482">NDIFF_CONTINUOUS = True         !   [Boolean] default = True</span>
<span id="L2483">                                ! If true, uses a continuous reconstruction of T and S when finding neutral</span>
<span id="L2484">                                ! surfaces along which diffusion will happen. If false, a PPM discontinuous</span>
<span id="L2485">                                ! reconstruction of T and S is done which results in a higher order routine but</span>
<span id="L2486">                                ! exacts a higher computational cost.</span>
<span id="L2487">NDIFF_REF_PRES = -1.0           !   [Pa] default = -1.0</span>
<span id="L2488">                                ! The reference pressure (Pa) used for the derivatives of the equation of state.</span>
<span id="L2489">                                ! If negative (default), local pressure is used.</span>
<span id="L2490">NDIFF_INTERIOR_ONLY = False     !   [Boolean] default = False</span>
<span id="L2491">                                ! If true, only applies neutral diffusion in the ocean interior.That is, the</span>
<span id="L2492">                                ! algorithm will exclude the surface and bottomboundary layers.</span>
<span id="L2493">NDIFF_USE_UNMASKED_TRANSPORT_BUG = False !   [Boolean] default = False</span>
<span id="L2494">                                ! If true, use an older form for the accumulation of neutral-diffusion</span>
<span id="L2495">                                ! transports that were unmasked, as used prior to Jan 2018. This is not</span>
<span id="L2496">                                ! recommended.</span>
<span id="L2497">NDIFF_ANSWER_DATE = 20240101    ! default = 99991231</span>
<span id="L2498">                                ! The vintage of the order of arithmetic to use for the neutral diffusion.</span>
<span id="L2499">                                ! Values of 20240330 or below recover the answers from the original form of the</span>
<span id="L2500">                                ! neutral diffusion code, while higher values use mathematically equivalent</span>
<span id="L2501">                                ! expressions that recover rotational symmetry.</span>
<span id="L2502"></span>
<span id="L2503">! === module MOM_hor_bnd_diffusion ===</span>
<span id="L2504">! This module implements horizontal diffusion of tracers near boundaries</span>
<span id="L2505">USE_HORIZONTAL_BOUNDARY_DIFFUSION = False !   [Boolean] default = False</span>
<span id="L2506">                                ! If true, enables the horizonal boundary tracer&#x27;s diffusion module.</span>
<span id="L2507">OBSOLETE_DIAGNOSTIC_IS_FATAL = True !   [Boolean] default = True</span>
<span id="L2508">                                ! If an obsolete diagnostic variable appears in the diag_table, cause a FATAL</span>
<span id="L2509">                                ! error rather than issue a WARNING.</span>
<span id="L2510"></span>
<span id="L2511">! === module MOM_sum_output ===</span>
<span id="L2512">CALCULATE_APE = True            !   [Boolean] default = True</span>
<span id="L2513">                                ! If true, calculate the available potential energy of the interfaces.  Setting</span>
<span id="L2514">                                ! this to false reduces the memory footprint of high-PE-count models</span>
<span id="L2515">                                ! dramatically.</span>
<span id="L2516">WRITE_STOCKS = True             !   [Boolean] default = True</span>
<span id="L2517">                                ! If true, write the integrated tracer amounts to stdout when the energy files</span>
<span id="L2518">                                ! are written.</span>
<span id="L2519">MAXTRUNC = 5000                 !   [truncations save_interval-1] default = 0</span>
<span id="L2520">                                ! The run will be stopped, and the day set to a very large value if the velocity</span>
<span id="L2521">                                ! is truncated more than MAXTRUNC times between energy saves.  Set MAXTRUNC to 0</span>
<span id="L2522">                                ! to stop if there is any truncation of velocities.</span>
<span id="L2523">MAX_ENERGY = 0.0                !   [m2 s-2] default = 0.0</span>
<span id="L2524">                                ! The maximum permitted average energy per unit mass; the model will be stopped</span>
<span id="L2525">                                ! if there is more energy than this.  If zero or negative, this is set to</span>
<span id="L2526">                                ! 10*MAXVEL^2.</span>
<span id="L2527">MAXVEL = 6.0                    !   [m s-1] default = 3.0E+08</span>
<span id="L2528">                                ! The maximum velocity allowed before the velocity components are truncated.</span>
<span id="L2529">ENERGYFILE = &quot;ocean.stats&quot;      ! default = &quot;ocean.stats&quot;</span>
<span id="L2530">                                ! The file to use to write the energies and globally summed diagnostics.</span>
<span id="L2531">DATE_STAMPED_STDOUT = True      !   [Boolean] default = True</span>
<span id="L2532">                                ! If true, use dates (not times) in messages to stdout</span>
<span id="L2533">ISO_DATE_STAMPED_STDOUT = False !   [Boolean] default = False</span>
<span id="L2534">                                ! If true, use ISO formatted dates in messages to stdout</span>
<span id="L2535">TIMEUNIT = 8.64E+04             !   [s] default = 8.64E+04</span>
<span id="L2536">                                ! The time unit in seconds a number of input fields</span>
<span id="L2537">READ_DEPTH_LIST = False         !   [Boolean] default = False</span>
<span id="L2538">                                ! Read the depth list from a file if it exists or create that file otherwise.</span>
<span id="L2539">DEPTH_LIST_MIN_INC = 1.0E-10    !   [m] default = 1.0E-10</span>
<span id="L2540">                                ! The minimum increment between the depths of the entries in the depth-list</span>
<span id="L2541">                                ! file.</span>
<span id="L2542">ENERGYSAVEDAYS = 0.5            !   [days] default = 1.0</span>
<span id="L2543">                                ! The interval in units of TIMEUNIT between saves of the energies of the run and</span>
<span id="L2544">                                ! other globally summed diagnostics.</span>
<span id="L2545">ENERGYSAVEDAYS_GEOMETRIC = 0.0  !   [days] default = 0.0</span>
<span id="L2546">                                ! The starting interval in units of TIMEUNIT for the first call to save the</span>
<span id="L2547">                                ! energies of the run and other globally summed diagnostics. The interval</span>
<span id="L2548">                                ! increases by a factor of 2. after each call to write_energy.</span>
<span id="L2549"></span>
<span id="L2550">! === module ocean_stochastics_init ===</span>
<span id="L2551">DO_SPPT = False                 !   [Boolean] default = False</span>
<span id="L2552">                                ! If true, then stochastically perturb the thermodynamic tendencies of T,S, amd</span>
<span id="L2553">                                ! h.  Amplitude and correlations are controlled by the nam_stoch namelist in the</span>
<span id="L2554">                                ! UFS model only.</span>
<span id="L2555">DO_SKEB = False                 !   [Boolean] default = False</span>
<span id="L2556">                                ! If true, then stochastically perturb the currents using the stochastic kinetic</span>
<span id="L2557">                                ! energy backscatter scheme.</span>
<span id="L2558">PERT_EPBL = False               !   [Boolean] default = False</span>
<span id="L2559">                                ! If true, then stochastically perturb the kinetic energy production and</span>
<span id="L2560">                                ! dissipation terms.  Amplitude and correlations are controlled by the nam_stoch</span>
<span id="L2561">                                ! namelist in the UFS model only.</span>
<span id="L2562"></span>
<span id="L2563">! === module MOM_surface_forcing ===</span>
<span id="L2564">VARIABLE_WINDS = True           !   [Boolean] default = True</span>
<span id="L2565">                                ! If true, the winds vary in time after the initialization.</span>
<span id="L2566">VARIABLE_BUOYFORCE = True       !   [Boolean] default = True</span>
<span id="L2567">                                ! If true, the buoyancy forcing varies in time after the initialization of the</span>
<span id="L2568">                                ! model.</span>
<span id="L2569">BUOY_CONFIG = &quot;file&quot;            ! default = &quot;zero&quot;</span>
<span id="L2570">                                ! The character string that indicates how buoyancy forcing is specified.  Valid</span>
<span id="L2571">                                ! options include (file), (data_override), (zero), (const), (linear), (MESO),</span>
<span id="L2572">                                ! (SCM_CVmix_tests), (BFB), (dumbbell), (USER) and (NONE).</span>
<span id="L2573">ARCHAIC_OMIP_FORCING_FILE = False !   [Boolean] default = True</span>
<span id="L2574">                                ! If true, use the forcing variable decomposition from the old German OMIP</span>
<span id="L2575">                                ! prescription that predated CORE. If false, use the variable groupings</span>
<span id="L2576">                                ! available from MOM output diagnostics of forcing variables.</span>
<span id="L2577">LONGWAVE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2578">                                ! The file with the longwave heat flux, in the variable given by</span>
<span id="L2579">                                ! LONGWAVE_FORCING_VAR.</span>
<span id="L2580">LONGWAVE_FORCING_VAR = &quot;LW&quot;     ! default = &quot;LW&quot;</span>
<span id="L2581">                                ! The variable with the longwave forcing field.</span>
<span id="L2582">LONGWAVE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2583">                                ! If positive the number of days of longwave fluxes per time level in</span>
<span id="L2584">                                ! LONGWAVE_FILE, or if negative the number of time levels per day.  If 31 change</span>
<span id="L2585">                                ! forcing monthly, or if 0 the model will guess the right value based on the</span>
<span id="L2586">                                ! file size.</span>
<span id="L2587">SHORTWAVE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2588">                                ! The file with the shortwave heat flux, in the variable given by</span>
<span id="L2589">                                ! SHORTWAVE_FORCING_VAR.</span>
<span id="L2590">SHORTWAVE_FORCING_VAR = &quot;SW&quot;    ! default = &quot;SW&quot;</span>
<span id="L2591">                                ! The variable with the shortwave forcing field.</span>
<span id="L2592">SHORTWAVE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2593">                                ! If positive the number of days of shortwave fluxes per time level in</span>
<span id="L2594">                                ! SHORTWAVE_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2595">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2596">                                ! the file size.</span>
<span id="L2597">EVAPORATION_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2598">                                ! The file with the evaporative moisture flux, in the variable given by</span>
<span id="L2599">                                ! EVAP_FORCING_VAR.</span>
<span id="L2600">EVAP_FORCING_VAR = &quot;evap&quot;       ! default = &quot;evap&quot;</span>
<span id="L2601">                                ! The variable with the evaporative moisture flux.</span>
<span id="L2602">EVAPORATION_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2603">                                ! If positive the number of days of evaporation per time level in</span>
<span id="L2604">                                ! EVAPORATION_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2605">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2606">                                ! the file size.</span>
<span id="L2607">LATENTHEAT_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2608">                                ! The file with the latent heat flux, in the variable given by</span>
<span id="L2609">                                ! LATENT_FORCING_VAR.</span>
<span id="L2610">LATENT_FORCING_VAR = &quot;latent&quot;   ! default = &quot;latent&quot;</span>
<span id="L2611">                                ! The variable with the latent heat flux.</span>
<span id="L2612">LATENTHEAT_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2613">                                ! If positive the number of days of latent heat fluxes per time level in</span>
<span id="L2614">                                ! LATENTHEAT_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2615">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2616">                                ! the file size.</span>
<span id="L2617">SENSIBLEHEAT_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2618">                                ! The file with the sensible heat flux, in the variable given by</span>
<span id="L2619">                                ! SENSIBLE_FORCING_VAR.</span>
<span id="L2620">SENSIBLE_FORCING_VAR = &quot;sensible&quot; ! default = &quot;sensible&quot;</span>
<span id="L2621">                                ! The variable with the sensible heat flux.</span>
<span id="L2622">SENSIBLEHEAT_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2623">                                ! If positive the number of days of sensible heat fluxes per time level in</span>
<span id="L2624">                                ! SENSIBLEHEAT_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2625">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2626">                                ! the file size.</span>
<span id="L2627">RAIN_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2628">                                ! The file with the liquid precipitation flux, in the variable given by</span>
<span id="L2629">                                ! RAIN_FORCING_VAR.</span>
<span id="L2630">RAIN_FORCING_VAR = &quot;liq_precip&quot; ! default = &quot;liq_precip&quot;</span>
<span id="L2631">                                ! The variable with the liquid precipitation flux.</span>
<span id="L2632">RAIN_FILE_DAYS_PER_RECORD = 0   ! default = 0</span>
<span id="L2633">                                ! If positive the number of days of rain fluxes per time level in RAIN_FILE, or</span>
<span id="L2634">                                ! if negative the number of time levels per day.  If 31 change forcing monthly,</span>
<span id="L2635">                                ! or if 0 the model will guess the right value based on the file size.</span>
<span id="L2636">SNOW_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2637">                                ! The file with the frozen precipitation flux, in the variable given by</span>
<span id="L2638">                                ! SNOW_FORCING_VAR.</span>
<span id="L2639">SNOW_FORCING_VAR = &quot;froz_precip&quot; ! default = &quot;froz_precip&quot;</span>
<span id="L2640">                                ! The variable with the frozen precipitation flux.</span>
<span id="L2641">RUNOFF_FILE = &quot;ocean_precip_monthly.nc&quot; !</span>
<span id="L2642">                                ! The file with the fresh and frozen runoff/calving fluxes, in variables given</span>
<span id="L2643">                                ! by LIQ_RUNOFF_FORCING_VAR and FROZ_RUNOFF_FORCING_VAR.</span>
<span id="L2644">LIQ_RUNOFF_FORCING_VAR = &quot;liq_runoff&quot; ! default = &quot;liq_runoff&quot;</span>
<span id="L2645">                                ! The variable with the liquid runoff flux.</span>
<span id="L2646">FROZ_RUNOFF_FORCING_VAR = &quot;froz_runoff&quot; ! default = &quot;froz_runoff&quot;</span>
<span id="L2647">                                ! The variable with the frozen runoff flux.</span>
<span id="L2648">RUNOFF_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2649">                                ! If positive the number of days of runoff per time level in RUNOFF_FILE, or if</span>
<span id="L2650">                                ! negative the number of time levels per day.  If 31 change forcing monthly, or</span>
<span id="L2651">                                ! if 0 the model will guess the right value based on the file size.</span>
<span id="L2652">SSTRESTORE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2653">                                ! The file with the SST toward which to restore in the variable given by</span>
<span id="L2654">                                ! SST_RESTORE_VAR.</span>
<span id="L2655">SALINITYRESTORE_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2656">                                ! The file with the surface salinity toward which to restore in the variable</span>
<span id="L2657">                                ! given by SSS_RESTORE_VAR.</span>
<span id="L2658">SST_RESTORE_VAR = &quot;SST&quot;         ! default = &quot;SST&quot;</span>
<span id="L2659">                                ! The variable with the SST toward which to restore.</span>
<span id="L2660">SSTRESTORE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2661">                                ! If positive the number of days of SST per time level in SSTRESTORE_FILE, or if</span>
<span id="L2662">                                ! negative the number of time levels per day.  If 31 change forcing monthly, or</span>
<span id="L2663">                                ! if 0 the model will guess the right value based on the file size.</span>
<span id="L2664">SSS_RESTORE_VAR = &quot;SSS&quot;         ! default = &quot;SSS&quot;</span>
<span id="L2665">                                ! The variable with the SSS toward which to restore.</span>
<span id="L2666">SALINITYRESTORE_FILE_DAYS_PER_RECORD = 0 ! default = 0</span>
<span id="L2667">                                ! If positive the number of days of salinity per time level in</span>
<span id="L2668">                                ! SALINITYRESTORE_FILE, or if negative the number of time levels per day.  If 31</span>
<span id="L2669">                                ! change forcing monthly, or if 0 the model will guess the right value based on</span>
<span id="L2670">                                ! the file size.</span>
<span id="L2671">WIND_CONFIG = &quot;file&quot;            ! default = &quot;zero&quot;</span>
<span id="L2672">                                ! The character string that indicates how wind forcing is specified.  Valid</span>
<span id="L2673">                                ! options include (file), (data_override), (2gyre), (1gyre), (gyres), (zero),</span>
<span id="L2674">                                ! (const), (Neverworld), (scurves), (ideal_hurr), (SCM_CVmix_tests) and (USER).</span>
<span id="L2675">WIND_FILE = &quot;ocean_forcing_daily.nc&quot; !</span>
<span id="L2676">                                ! The file in which the wind stresses are found in variables STRESS_X and</span>
<span id="L2677">                                ! STRESS_Y.</span>
<span id="L2678">WINDSTRESS_X_VAR = &quot;taux&quot;       ! default = &quot;STRESS_X&quot;</span>
<span id="L2679">                                ! The name of the x-wind stress variable in WIND_FILE.</span>
<span id="L2680">WINDSTRESS_Y_VAR = &quot;tauy&quot;       ! default = &quot;STRESS_Y&quot;</span>
<span id="L2681">                                ! The name of the y-wind stress variable in WIND_FILE.</span>
<span id="L2682">WIND_STAGGER = &quot;C&quot;              ! default = &quot;C&quot;</span>
<span id="L2683">                                ! A character indicating how the wind stress components are staggered in</span>
<span id="L2684">                                ! WIND_FILE.  This may be A or C for now.</span>
<span id="L2685">WINDSTRESS_SCALE = 1.0          !   [nondim] default = 1.0</span>
<span id="L2686">                                ! A value by which the wind stresses in WIND_FILE are rescaled.</span>
<span id="L2687">USTAR_FORCING_VAR = &quot;&quot;          ! default = &quot;&quot;</span>
<span id="L2688">                                ! The name of the friction velocity variable in WIND_FILE or blank to get ustar</span>
<span id="L2689">                                ! from the wind stresses plus the gustiness.</span>
<span id="L2690">WIND_FILE_DAYS_PER_RECORD = 0   ! default = 0</span>
<span id="L2691">                                ! If positive the number of days of wind stress per time level in WIND_FILE, or</span>
<span id="L2692">                                ! if negative the number of time levels per day.  If 31 change forcing monthly,</span>
<span id="L2693">                                ! or if 0 the model will guess the right value based on the file size.</span>
<span id="L2694">RESTOREBUOY = True              !   [Boolean] default = False</span>
<span id="L2695">                                ! If true, the buoyancy fluxes drive the model back toward some specified</span>
<span id="L2696">                                ! surface state with a rate given by FLUXCONST.</span>
<span id="L2697">LATENT_HEAT_FUSION = 3.34E+05   !   [J/kg] default = 3.34E+05</span>
<span id="L2698">                                ! The latent heat of fusion.</span>
<span id="L2699">LATENT_HEAT_VAPORIZATION = 2.5E+06 !   [J/kg] default = 2.5E+06</span>
<span id="L2700">                                ! The latent heat of fusion.</span>
<span id="L2701">FLUXCONST = 0.5                 !   [m day-1] default = 0.0</span>
<span id="L2702">                                ! The constant that relates the restoring surface fluxes to the relative surface</span>
<span id="L2703">                                ! anomalies (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2704">FLUXCONST_T = 0.5               !   [m day-1] default = 0.5</span>
<span id="L2705">                                ! The constant that relates the restoring surface temperature flux to the</span>
<span id="L2706">                                ! relative surface anomaly (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2707">FLUXCONST_S = 0.5               !   [m day-1] default = 0.5</span>
<span id="L2708">                                ! The constant that relates the restoring surface salinity flux to the relative</span>
<span id="L2709">                                ! surface anomaly (akin to a piston velocity).  Note the non-MKS units.</span>
<span id="L2710">RESTORE_FLUX_RHO = 1035.0       !   [kg m-3] default = 1035.0</span>
<span id="L2711">                                ! The density that is used to convert piston velocities into salt or heat fluxes</span>
<span id="L2712">                                ! with RESTORE_SALINITY or RESTORE_TEMPERATURE.</span>
<span id="L2713">GUST_CONST = 0.0                !   [Pa] default = 0.0</span>
<span id="L2714">                                ! The background gustiness in the winds.</span>
<span id="L2715">USTAR_GUSTLESS_BUG = False      !   [Boolean] default = False</span>
<span id="L2716">                                ! If true include a bug in the time-averaging of the gustless wind friction</span>
<span id="L2717">                                ! velocity</span>
<span id="L2718">READ_GUST_2D = True             !   [Boolean] default = False</span>
<span id="L2719">                                ! If true, use a 2-dimensional gustiness supplied from an input file</span>
<span id="L2720">GUST_2D_FILE = &quot;gustiness_qscat.nc&quot; !</span>
<span id="L2721">                                ! The file in which the wind gustiness is found in variable gustiness.</span>
<span id="L2722"></span>
<span id="L2723">! === module MOM_restart ===</span>
<span id="L2724">USE_WAVES = False               !   [Boolean] default = False</span>
<span id="L2725">                                ! If true, enables surface wave modules.</span>
<span id="L2726"></span>
<span id="L2727">! === module MOM_main (MOM_driver) ===</span>
<span id="L2728">DT_FORCING = 7200.0             !   [s] default = 3600.0</span>
<span id="L2729">                                ! The time step for changing forcing, coupling with other components, or</span>
<span id="L2730">                                ! potentially writing certain diagnostics. The default value is given by DT.</span>
<span id="L2731">DAYMAX = 1.0                    !   [days]</span>
<span id="L2732">                                ! The final time of the whole simulation, in units of TIMEUNIT seconds.  This</span>
<span id="L2733">                                ! also sets the potential end time of the present run segment if the end time is</span>
<span id="L2734">                                ! not set via ocean_solo_nml in input.nml.</span>
<span id="L2735">SINGLE_STEPPING_CALL = True     !   [Boolean] default = True</span>
<span id="L2736">                                ! If true, advance the state of MOM with a single step including both dynamics</span>
<span id="L2737">                                ! and thermodynamics.  If false the two phases are advanced with separate calls.</span>
<span id="L2738">RESTART_CONTROL = 3             ! default = 1</span>
<span id="L2739">                                ! An integer whose bits encode which restart files are written. Add 2 (bit 1)</span>
<span id="L2740">                                ! for a time-stamped file, and odd (bit 0) for a non-time-stamped file. A</span>
<span id="L2741">                                ! non-time-stamped restart file is saved at the end of the run segment for any</span>
<span id="L2742">                                ! non-negative value.</span>
<span id="L2743">RESTINT = 365.0                 !   [days] default = 0.0</span>
<span id="L2744">                                ! The interval between saves of the restart file in units of TIMEUNIT.  Use 0</span>
<span id="L2745">                                ! (the default) to not save incremental restart files at all.</span>
<span id="L2746">WRITE_CPU_STEPS = 1000          ! default = 1000</span>
<span id="L2747">                                ! The number of coupled timesteps between writing the cpu time. If this is not</span>
<span id="L2748">                                ! positive, do not check cpu time, and the segment run-length can not be set via</span>
<span id="L2749">                                ! an elapsed CPU time.</span>
<span id="L2750"></span>
<span id="L2751">! === module MOM_write_cputime ===</span>
<span id="L2752">MAXCPU = 2.88E+04               !   [wall-clock seconds] default = -1.0</span>
<span id="L2753">                                ! The maximum amount of cpu time per processor for which MOM should run before</span>
<span id="L2754">                                ! saving a restart file and quitting with a return value that indicates that a</span>
<span id="L2755">                                ! further run is required to complete the simulation. If automatic restarts are</span>
<span id="L2756">                                ! not desired, use a negative value for MAXCPU.  MAXCPU has units of wall-clock</span>
<span id="L2757">                                ! seconds, so the actual CPU time used is larger by a factor of the number of</span>
<span id="L2758">                                ! processors used.</span>
<span id="L2759">CPU_TIME_FILE = &quot;CPU_stats&quot;     ! default = &quot;CPU_stats&quot;</span>
<span id="L2760">                                ! The file into which CPU time is written.</span>
<span id="L2761"></span>
<span id="L2762">! === module MOM_file_parser ===</span>
<span id="L2763">SEND_LOG_TO_STDOUT = False      !   [Boolean] default = False</span>
<span id="L2764">                                ! If true, all log messages are also sent to stdout.</span>
<span id="L2765">DOCUMENT_FILE = &quot;MOM_parameter_doc&quot; ! default = &quot;MOM_parameter_doc&quot;</span>
<span id="L2766">                                ! The basename for files where run-time parameters, their settings, units and</span>
<span id="L2767">                                ! defaults are documented. Blank will disable all parameter documentation.</span>
<span id="L2768">COMPLETE_DOCUMENTATION = True   !   [Boolean] default = True</span>
<span id="L2769">                                ! If true, all run-time parameters are documented in MOM_parameter_doc.all .</span>
<span id="L2770">MINIMAL_DOCUMENTATION = True    !   [Boolean] default = True</span>
<span id="L2771">                                ! If true, non-default run-time parameters are documented in</span>
<span id="L2772">                                ! MOM_parameter_doc.short .</span>
</pre>
